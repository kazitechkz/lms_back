from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.test.test_dto import TestRDTO
from app.adapters.repositories.test.test_repository import TestRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetTestCase(BaseUseCase[TestRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = TestRepository(db)

    async def execute(self, test_id: int) -> TestRDTO:
        test = await self.validate(test_id=test_id)
        return TestRDTO.from_orm(test)

    async def validate(self, test_id: int):
        test = await self.repository.get(test_id)
        if not test:
            raise AppExceptionResponse.not_found("Тест не найден")
        return test
