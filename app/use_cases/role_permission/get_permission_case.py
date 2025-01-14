from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.permission.permission_dto import PermissionRDTO
from app.adapters.repositories.permission.permission_repository import PermissionRepository
from app.adapters.repositories.role.role_repository import RoleRepository
from app.adapters.repositories.role_permission.role_permission_repository import RolePermissionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetRolePermissionCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = RolePermissionRepository(db)
        self.role_repository = RoleRepository(db)
        self.permission_repository = PermissionRepository(db)

    async def execute(self, role_id: int) -> list[PermissionRDTO]:
        return await self.validate(role_id=role_id)

    async def validate(self, role_id: int):
        if await self.role_repository.get(id=role_id) is None:
            raise AppExceptionResponse.bad_request(message="Роль не найдена")
        role_permissions = await self.repository.get_with_filters(filters=[
            and_(self.repository.model.role_id == role_id)
        ])
        permissions = []
        for rp in role_permissions:
            permission = await self.permission_repository.get(rp.permission_id)
            if permission:
                permissions.append(permission)
        return [PermissionRDTO.from_orm(p) for p in permissions]
