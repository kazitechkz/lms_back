from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question.question_dto import QuestionRDTO, QuestionCDTO
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.adapters.repositories.test.test_repository import TestRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateQuestionCase(BaseUseCase[QuestionRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = QuestionRepository(db)
        self.test_repository = TestRepository(db)

    async def execute(self, dto: QuestionCDTO) -> QuestionRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return QuestionRDTO.from_orm(data)

    async def validate(self, dto: QuestionCDTO):
        if await self.test_repository.get(id=dto.test_id) is None:
            raise AppExceptionResponse.bad_request(message="Тест не найден")
        return self.repository.model(**dto.dict())
