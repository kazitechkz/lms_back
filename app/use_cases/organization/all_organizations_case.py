from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.organization.organization_dto import OrganizationRDTOWithRelated
from app.adapters.dto.pagination_dto import PaginationOrganizations
from app.adapters.filters.organization.organization_filter import OrganizationFilter
from app.adapters.repositories.organization.organization_repository import OrganizationRepository
from app.use_cases.base_case import BaseUseCase


class AllOrganizationsCase(BaseUseCase[PaginationOrganizations]):
    def __init__(self, db: AsyncSession):
        self.repository = OrganizationRepository(db)

    async def execute(self, params: OrganizationFilter):
        organizations = await self.repository.paginate(
            dto=OrganizationRDTOWithRelated,
            page=params.page,
            per_page=params.per_page,
            options=[
                joinedload(self.repository.model.type)
            ]
        )
        return organizations

    async def validate(self):
        pass
