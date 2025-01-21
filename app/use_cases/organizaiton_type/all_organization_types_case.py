from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.organization_type.organization_type_dto import OrganizationTypeRDTO
from app.adapters.repositories.organization_type.organization_type_repository import OrganizationTypeRepository
from app.use_cases.base_case import BaseUseCase


class AllOrganizationTypesCase(BaseUseCase[List[OrganizationTypeRDTO]]):
    def __init__(self, db: AsyncSession):
        self.repository = OrganizationTypeRepository(db)

    async def execute(self) -> List[OrganizationTypeRDTO]:
        org_types = await self.repository.get_all()
        return [OrganizationTypeRDTO.from_orm(org) for org in org_types]

    async def validate(self):
        pass
