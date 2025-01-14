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
        # Валидация входных данных
        await self.validate(role_id=role_id, permission_ids=permission_ids)

        # Получаем текущие разрешения роли
        current_permissions = await self.repository.get_with_filters(filters=[
            and_(self.repository.model.role_id == role_id)
        ])
        current_permission_ids = {rp.permission_id for rp in current_permissions}

        # Разделяем разрешения на добавляемые и удаляемые
        to_add = set(permission_ids) - current_permission_ids
        to_remove = current_permission_ids - set(permission_ids)

        # Добавляем новые разрешения
        for permission_id in to_add:
            obj = RolePermissionCDTO(role_id=role_id, permission_id=permission_id)
            await self.repository.create(obj=self.repository.model(**obj.dict()))

        # Удаляем лишние разрешения
        for permission_id in to_remove:
            await self.repository.delete_with_filters(filters=[
                and_(
                    self.repository.model.role_id == role_id,
                    self.repository.model.permission_id == permission_id
                )
            ])

        # Возвращаем обновленный список разрешений
        updated_permissions = await self.repository.get_with_filters(filters=[
            and_(self.repository.model.role_id == role_id)
        ])
        return [RolePermissionRDTO.from_orm(rp) for rp in updated_permissions]

    async def validate(self, role_id: int, permission_ids: list[int]):
        # Проверка, существует ли роль
        if await self.role_repository.get(id=role_id) is None:
            raise AppExceptionResponse.bad_request(message="Роль не найдена")

        # Проверка, существуют ли все разрешения
        for permission_id in permission_ids:
            if await self.permission_repository.get(id=permission_id) is None:
                raise AppExceptionResponse.bad_request(message=f"Право с ID {permission_id} не найдено")
