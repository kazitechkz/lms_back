from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.test_type.tag_type_dto import TestTypeRDTO
from app.adapters.repositories.test_type.test_type_repository import TestTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetTestTypeCase(BaseUseCase[TestTypeRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = TestTypeRepository(db)

    async def execute(self, test_type_id: int) -> TestTypeRDTO:
        test_type = await self.validate(test_type_id=test_type_id)
        return TestTypeRDTO.from_orm(test_type)

    async def validate(self, test_type_id: int):
        test_type = await self.repository.get(test_type_id)
        if not test_type:
            raise AppExceptionResponse.not_found("Тип не найден")
        return test_type
