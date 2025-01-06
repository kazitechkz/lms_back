from typing import List

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role_permission.role_permission_dto import RolePermissionCDTO, RolePermissionRDTO
from app.adapters.repositories.permission.permission_repository import PermissionRepository
from app.adapters.repositories.role.role_repository import RoleRepository
from app.adapters.repositories.role_permission.role_permission_repository import RolePermissionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateRolePermissionCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = RolePermissionRepository(db)
        self.role_repository = RoleRepository(db)
        self.permission_repository = PermissionRepository(db)

    async def execute(self, role_id: int, permission_ids: list[int]) -> list[RolePermissionRDTO]:
        await self.validate(role_id=role_id, permission_ids=permission_ids)
        for permission in permission_ids:
            obj = RolePermissionCDTO(role_id=role_id, permission_id=permission)
            if await self.repository.get_first_with_filters(filters=[
                and_(
                    self.repository.model.role_id == obj.role_id,
                    self.repository.model.permission_id == obj.permission_id
                )
            ]) is None:
                await self.repository.create(obj=self.repository.model(**obj.dict()))
        rps = await self.repository.get_with_filters(filters=[and_(self.repository.model.role_id == role_id)])
        return [RolePermissionRDTO.from_orm(rp) for rp in rps]

    async def validate(self, role_id: int, permission_ids: list[int]):
        if await self.role_repository.get(id=role_id) is None:
            raise AppExceptionResponse.bad_request(message="Роль не найдена")
        for permission_id in permission_ids:
            if await self.permission_repository.get(id=permission_id) is None:
                raise AppExceptionResponse.bad_request(message="Права не найдены")
