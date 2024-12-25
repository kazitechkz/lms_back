from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.repositories.role.role_repository import RoleRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetRoleByValueCase(BaseUseCase[RoleRDTO]):
    def __init__(self, db: AsyncSession):
        self.role_repository = RoleRepository(db)

    async def execute(self, role_value: str) -> RoleRDTO:
        role = await self.validate(role_value=role_value)
        return RoleRDTO.from_orm(role)

    async def validate(self, role_value: str):
        filters = [self.role_repository.model.value == role_value]
        role = await self.role_repository.get_first_with_filters(filters)
        if not role:
            raise AppExceptionResponse.not_found("Роль не найдена")
        return role
