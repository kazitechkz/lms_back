from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.organization.organization_dto import OrganizationRDTOWithRelated
from app.adapters.repositories.organization.organization_repository import OrganizationRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetOrganizationCase(BaseUseCase[OrganizationRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = OrganizationRepository(db)

    async def execute(self, organization_id: int) -> OrganizationRDTOWithRelated:
        organization = await self.validate(organization_id=organization_id)
        return OrganizationRDTOWithRelated.from_orm(organization)

    async def validate(self, organization_id: int):
        organization = await self.repository.get(organization_id, options=[
            joinedload(self.repository.model.type)
        ])
        if not organization:
            raise AppExceptionResponse.not_found("Организация не найдена")
        return organization
