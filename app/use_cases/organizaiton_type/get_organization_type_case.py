from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.organization_type.organization_type_dto import OrganizationTypeRDTO
from app.adapters.repositories.organization_type.organization_type_repository import OrganizationTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetOrganizationTypeCase(BaseUseCase[OrganizationTypeRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = OrganizationTypeRepository(db)

    async def execute(self, org_type_id: int) -> OrganizationTypeRDTO:
        org_type = await self.validate(org_type_id=org_type_id)
        return OrganizationTypeRDTO.from_orm(org_type)

    async def validate(self, org_type_id: int):
        org_type = await self.repository.get(org_type_id)
        if not org_type:
            raise AppExceptionResponse.not_found("Тип не найден")
        return org_type
