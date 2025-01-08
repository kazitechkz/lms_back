from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question.question_dto import QuestionRDTO, QuestionRDTOWithRelated
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.adapters.repositories.test.test_repository import TestRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetQuestionByTestCase(BaseUseCase[list[QuestionRDTO]]):

    def __init__(self, db: AsyncSession):
        self.repository = QuestionRepository(db)
        self.test_repository = TestRepository(db)

    async def execute(self, test_id: int) -> list[QuestionRDTO]:
        questions = await self.validate(test_id=test_id)
        return [QuestionRDTO.from_orm(question) for question in questions]

    async def validate(self, test_id: int):
        if await self.test_repository.get(id=test_id) is None:
            raise AppExceptionResponse.bad_request(message="Тест не найден")
        questions = await self.repository.get_with_filters(filters=[
            and_(self.repository.model.test_id == test_id)
        ])
        return questions
