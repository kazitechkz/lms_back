from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.organization_type.organization_type_dto import OrganizationTypeRDTO
from app.adapters.repositories.organization_type.organization_type_repository import OrganizationTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetOrganizationTypeByValueCase(BaseUseCase[OrganizationTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.org_type_repository = OrganizationTypeRepository(db)

    async def execute(self, org_type_value: str) -> OrganizationTypeRDTO:
        org_type = await self.validate(org_type_value=org_type_value)
        return OrganizationTypeRDTO.from_orm(org_type)

    async def validate(self, org_type_value: str):
        filters = [self.org_type_repository.model.value == org_type_value]
        org_type = await self.org_type_repository.get_first_with_filters(filters)
        if not org_type:
            raise AppExceptionResponse.not_found("Тип не найден")
        return org_type
