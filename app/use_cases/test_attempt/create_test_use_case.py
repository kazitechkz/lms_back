from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.test_attempt.test_attempt_dto import TestAttemptRDTO, TestAttemptCDTO
from app.adapters.repositories.test.test_repository import TestRepository
from app.adapters.repositories.test_attempt.test_attempt_repository import TestAttemptRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateTestUseCase(BaseUseCase[TestAttemptRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = TestAttemptRepository(db)
        self.test_repository = TestRepository(db)

    async def execute(self, dto: TestAttemptCDTO) -> TestAttemptRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return TestAttemptRDTO.from_orm(data)

    async def validate(self, dto: TestAttemptCDTO):
        if await self.test_repository.get(id=dto.test_id) is None:
            raise AppExceptionResponse.bad_request(message="Тест не найден")
