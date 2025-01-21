from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.organization_type.organization_type_dto import OrganizationTypeRDTO, OrganizationTypeCDTO
from app.adapters.repositories.organization_type.organization_type_repository import OrganizationTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateOrganizationTypeCase(BaseUseCase[OrganizationTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = OrganizationTypeRepository(db)

    async def execute(self, dto: OrganizationTypeCDTO) -> OrganizationTypeRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return OrganizationTypeRDTO.from_orm(data)

    async def validate(self, dto: OrganizationTypeCDTO):
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Тип с таким значением уже существует"
            )
        return self.repository.model(**dto.dict())
