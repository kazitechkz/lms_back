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
        # Validate all DTOs for the single question
        objs = await self.validate(dtos=dtos)
        # Create all objects in the repository
        data = await self.repository.create_many(objs=objs)
        # Return the results as a list of AnswerRDTO
        return [AnswerRDTO.from_orm(item) for item in data]

    async def validate(self, dtos: list[AnswerCDTO]):
        if not dtos:
            raise AppExceptionResponse.bad_request(message="Список ответов пуст.")

        # All answers are for the same question, get the question ID
        question_id = dtos[0].question_id
        question = await self.question_repository.get(id=question_id)
        if question is None:
            raise AppExceptionResponse.bad_request(message="Вопрос не найден.")

        # Validate characteristics
        characteristic_ids = {dto.characteristic_id for dto in dtos if dto.characteristic_id}
        if characteristic_ids:
            characteristics = {c.id for c in
                               await self.characteristic_repository.get_many(ids=list(characteristic_ids))}
            missing_characteristics = characteristic_ids - characteristics
            if missing_characteristics:
                raise AppExceptionResponse.bad_request(message="Одна или несколько характеристик не найдены.")

        # Validate correct answer constraints for the question
        if question.type_id == 1:
            correct_answers = [dto for dto in dtos if dto.is_correct]
            if len(correct_answers) > 1:
                raise AppExceptionResponse.bad_request(
                    message="Для данного вопроса может быть только один правильный ответ."
                )

        for dto in dtos:
            if dto.is_correct:
                if question.type_id == 1:
                    dto.points = 1
                elif question.type_id == 2 and dto.points > question.points:
                    raise AppExceptionResponse.bad_request(
                        message=(
                            "Баллы за ответ не могут превышать "
                            "баллов, предусмотренных за сам вопрос."
                        )
                    )
            else:
                if question.type_id == 1:
                    dto.points = 0
                elif question.type_id == 2 and dto.points < 0:
                    raise AppExceptionResponse.bad_request(
                        message=(
                            "Баллы за ответ не могут быть отрицательными."
                        )
                    )
        # Convert DTOs to repository models
        return [self.repository.model(**dto.dict()) for dto in dtos]
