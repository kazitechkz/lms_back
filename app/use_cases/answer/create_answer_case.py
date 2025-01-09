from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.answer.answer_dto import AnswerRDTO, AnswerCDTO
from app.adapters.repositories.answer.answer_repository import AnswerRepository
from app.adapters.repositories.characteristic.characteristic_repository import CharacteristicRepository
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateAnswerCase(BaseUseCase[AnswerRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = AnswerRepository(db)
        self.question_repository = QuestionRepository(db)
        self.characteristic_repository = CharacteristicRepository(db)

    async def execute(self, dtos: list[AnswerCDTO]) -> list[AnswerRDTO]:
        await self.validate(dtos=dtos)

        existing_answers = await self.repository.get_with_filters(filters=[
            self.repository.model.question_id == dtos[0].question_id
        ])

        for obj in dtos:
            existing_answer = next((answer for answer in existing_answers if answer.text == obj.text),
                                   None)
            if existing_answer:
                await self.repository.update(obj=existing_answer, dto=obj)
            else:
                await self.repository.create(obj=self.repository.model(**obj.dict()))

        updated_answers = await self.repository.get_with_filters(filters=[
            self.repository.model.question_id == dtos[0].question_id
        ])

        return [AnswerRDTO.from_orm(item) for item in updated_answers]

    async def validate(self, dtos: list[AnswerCDTO]):
        if not dtos:
            raise AppExceptionResponse.bad_request(message="Список ответов пуст.")

        question_id = dtos[0].question_id
        question = await self.question_repository.get(id=question_id)
        if question is None:
            raise AppExceptionResponse.bad_request(message="Вопрос не найден.")

        if question.type_id == 1:
            await self.validate_single_choice(dtos)
        elif question.type_id == 2:
            await self.validate_multiple_choice(dtos)
        elif question.type_id == 3:
            await self.validate_characteristics(dtos)

        self.validate_duplicates(dtos)

        return [self.repository.model(**dto.dict()) for dto in dtos]

    async def validate_characteristics(self, dtos: list[AnswerCDTO]):
        for dto in dtos:
            if dto.points is None or dto.points < 0:
                raise AppExceptionResponse.bad_request(
                    message="Баллы для психологического теста не могут быть отрицательными или отсутствовать."
                )
        characteristic_ids = {dto.characteristic_id for dto in dtos if dto.characteristic_id}
        if characteristic_ids:
            characteristics = {c.id for c in
                               await self.characteristic_repository.get_many(ids=list(characteristic_ids))}
            missing_characteristics = characteristic_ids - characteristics
            if missing_characteristics:
                raise AppExceptionResponse.bad_request(message="Одна или несколько характеристик не найдены.")

    async def validate_single_choice(self, dtos: list[AnswerCDTO]):
        correct_answers = [dto for dto in dtos if dto.is_correct]
        if len(correct_answers) > 1:
            raise AppExceptionResponse.bad_request(
                message="Для данного вопроса может быть только один правильный ответ."
            )

        for dto in dtos:
            dto.points = 1 if dto.is_correct else 0

    async def validate_multiple_choice(self, dtos: list[AnswerCDTO]):
        correct_answers = [dto for dto in dtos if dto.is_correct]
        if len(correct_answers) > 3:
            raise AppExceptionResponse.bad_request(message="Количество правильных ответов не должно превышать 3.")

        for dto in dtos:
            dto.points = 1 if dto.is_correct else 0

    def validate_duplicates(self, dtos: list[AnswerCDTO]):
        answer_texts = [dto.text for dto in dtos]
        if len(answer_texts) != len(set(answer_texts)):
            raise AppExceptionResponse.bad_request(message="Ответы не должны повторяться.")

