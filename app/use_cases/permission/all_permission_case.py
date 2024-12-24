from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.permission.permission_dto import PermissionRDTO
from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.repositories.permission.permission_repository import PermissionRepository
from app.use_cases.base_case import BaseUseCase


class AllPermissionCase(BaseUseCase[List[PermissionRDTO]]):
    def __init__(self, db: AsyncSession):
        self.permission_repository = PermissionRepository(db)

    async def execute(self) -> List[PermissionRDTO]:
        permissions = await self.permission_repository.get_all()
        return [PermissionRDTO.from_orm(permission) for permission in permissions]

    async def validate(self):
        pass
