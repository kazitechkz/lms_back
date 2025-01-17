from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question.question_dto import QuestionRDTO, QuestionUDTO
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.adapters.repositories.test.test_repository import TestRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateQuestionCase(BaseUseCase[QuestionRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = QuestionRepository(db)
        self.test_repository = TestRepository(db)

    async def execute(self, id: int, dto: QuestionUDTO) -> QuestionRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return QuestionRDTO.from_orm(data)

    async def validate(self, id: int, dto: QuestionUDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Тест не найден")
        if await self.test_repository.get(id=dto.test_id) is None:
            raise AppExceptionResponse.bad_request(message="Тест не найден")

        return existed
