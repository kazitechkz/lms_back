from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.permission.permission_dto import PermissionRDTO
from app.adapters.repositories.permission.permission_repository import PermissionRepository
from app.use_cases.base_case import BaseUseCase


class GetPermissionByValueCase(BaseUseCase[PermissionRDTO]):
    def __init__(self, db: AsyncSession):
        self.permission_repository = PermissionRepository(db)

    async def execute(self, permission_value: str) -> PermissionRDTO:
        filters = [self.permission_repository.model.value == permission_value]
        permission = await self.permission_repository.get_first_with_filters(filters)
        if not permission:
            raise ValueError("Право не найдено")
        return PermissionRDTO.from_orm(permission)

    async def validate(self):
        pass