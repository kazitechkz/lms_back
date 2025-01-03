from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.organization.organization_dto import OrganizationRDTOWithRelated
from app.adapters.repositories.organization.organization_repository import OrganizationRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetOrganizationByValueCase(BaseUseCase[OrganizationRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = OrganizationRepository(db)

    async def execute(self, bin: str) -> OrganizationRDTOWithRelated:
        organization = await self.validate(bin=bin)
        return OrganizationRDTOWithRelated.from_orm(organization)

    async def validate(self, bin: str):
        if len(bin) != 12:
            raise AppExceptionResponse.bad_request(message="БИН должен состоять из 12 цифр")
        filters = [self.repository.model.bin == bin]
        organization = await self.repository.get_first_with_filters(filters, options=[
            joinedload(self.repository.model.type)
        ])
        if not organization:
            raise AppExceptionResponse.bad_request(message="Организация не найдена")
        return organization
