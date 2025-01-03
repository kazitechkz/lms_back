from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.organization.organization_dto import OrganizationRDTOWithRelated, OrganizationCDTO
from app.adapters.repositories.organization.organization_repository import OrganizationRepository
from app.adapters.repositories.organization_type.organization_type_repository import OrganizationTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateOrganizationCase(BaseUseCase[OrganizationRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = OrganizationRepository(db)
        self.type_repository = OrganizationTypeRepository(db)

    async def execute(self, dto: OrganizationCDTO) -> OrganizationRDTOWithRelated:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj, options=[
            joinedload(self.repository.model.type)
        ])
        return OrganizationRDTOWithRelated.from_orm(data)

    async def validate(self, dto: OrganizationCDTO):
        if len(dto.bin) != 12:
            raise AppExceptionResponse.bad_request("БИН должен содержать 12 цифр")
        if await self.repository.get_first_with_filters(filters=[
            and_(self.repository.model.bin == dto.bin)
        ]) is not None:
            raise AppExceptionResponse.bad_request(
                "Организация с таким БИН номером уже существует"
            )
        if await self.type_repository.get(id=dto.type_id) is None:
            raise AppExceptionResponse.bad_request("Тип организации не найден")
        return self.repository.model(**dto.dict())
