from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.question_attempt.question_attempt_dto import QuestionAttemptRDTO, QuestionAttemptCDTO, \
    MultipleAnswerCDTO, PsychologicalAnswerCDTO
from app.adapters.dto.test_attempt.test_attempt_dto import TestAttemptCDTO
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.repositories.answer.answer_repository import AnswerRepository
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.adapters.repositories.question_attempt.question_attempt_repository import QuestionAttemptRepository
from app.adapters.repositories.test.test_repository import TestRepository
from app.adapters.repositories.test_attempt.test_attempt_repository import TestAttemptRepository
from app.core.app_exception_response import AppExceptionResponse
from app.entities.test import QuestionModel
from app.use_cases.base_case import BaseUseCase


class PsychologicalAnswerUseCase(BaseUseCase[QuestionAttemptRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = QuestionAttemptRepository(db)
        self.answer_repository = AnswerRepository(db)
        self.question_repository = QuestionRepository(db)
        self.test_repository = TestRepository(db)
        self.test_attempt_repository = TestAttemptRepository(db)

    async def execute(self, dto: PsychologicalAnswerCDTO, user: UserRDTOWithRelated) -> QuestionAttemptRDTO:
        question = await self.validate(dto=dto)
        total_points = 0
        if dto.answer_ids:
            answers = await self.answer_repository.get_with_filters(filters=[
                self.answer_repository.model.id.in_(dto.answer_ids),
                self.answer_repository.model.question_id == dto.question_id
            ])
            for answer in answers:
                total_points += answer.points
            if not answers:
                raise AppExceptionResponse.bad_request(message="Ответы не найдены")

        obj = QuestionAttemptCDTO(
            test_id=question.test_id,
            question_id=dto.question_id,
            user_id=user.id,
            answer_ids=dto.answer_ids,
            is_correct=False,
            point=total_points
        )

        result = await self.repository.get_first_with_filters(filters=[
            and_(self.repository.model.question_id == dto.question_id)
        ])

        if result:
            data = await self.repository.update(obj=result, dto=obj)
        else:
            data = await self.repository.create(obj=self.repository.model(**obj.dict()))


        if dto.is_last:
            print("Test finished logic")
            points = await self.calculate_points(test_id=question.test_id)
            test_attempt_dto = TestAttemptCDTO(
                test_id=question.test_id,
                user_id=user.id,
                point=points,
                is_success=True
            )

            test_attempt = await self.test_attempt_repository.get_first_with_filters(filters=[
                and_(self.test_attempt_repository.model.test_id == question.test_id)
            ])

            if test_attempt:
                await self.test_attempt_repository.update(obj=test_attempt, dto=test_attempt_dto)
            else:
                await self.test_attempt_repository.create(
                    obj=self.test_attempt_repository.model(**test_attempt_dto.dict()))

        return QuestionAttemptRDTO.from_orm(data)

    async def validate(self, dto: MultipleAnswerCDTO):
        question = await self.question_repository.get(id=dto.question_id)
        if question is None:
            raise AppExceptionResponse.bad_request(message="Вопрос не найден")
        return question

    async def calculate_points(self, test_id: int):
        results = await self.repository.get_with_filters(filters=[
            and_(self.repository.model.test_id == test_id)
        ])
        total_points = 0
        for result in results:
            total_points += result.point

        return total_points

