from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.test_type.tag_type_dto import TestTypeRDTO, TestTypeCDTO
from app.adapters.repositories.test_type.test_type_repository import TestTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateTestTypeCase(BaseUseCase[TestTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = TestTypeRepository(db)

    async def execute(self, dto: TestTypeCDTO) -> TestTypeRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return TestTypeRDTO.from_orm(data)

    async def validate(self, dto: TestTypeCDTO):
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Тип с таким значением уже существует"
            )
        return self.repository.model(**dto.dict())
