from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.test.test_dto import TestRDTO, TestRDTOWithRelated
from app.adapters.repositories.test.test_repository import TestRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetTestCase(BaseUseCase[TestRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = TestRepository(db)

    async def execute(self, test_id: int) -> TestRDTOWithRelated:
        test = await self.validate(test_id=test_id)
        return TestRDTOWithRelated.from_orm(test)

    async def validate(self, test_id: int):
        test = await self.repository.get(test_id, options=[
            selectinload(self.repository.model.video),
            selectinload(self.repository.model.course),
            selectinload(self.repository.model.type)
        ])
        if not test:
            raise AppExceptionResponse.not_found("Тест не найден")
        return test
