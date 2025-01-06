from fastapi import APIRouter, Depends, Form, Body
from pydantic import Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role_permission.role_permission_dto import RolePermissionRDTO
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.role_permission.create_permission_case import CreateRolePermissionCase
from app.use_cases.role_permission.delete_permission_case import DeleteRolePermissionCase


class RolePermissionApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.post(
            "/create",
            response_model=list[RolePermissionRDTO],
            summary="Создать право для роли",
            description="Создание прав для ролей",
        )(self.create)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить право для роли по уникальному ID",
            description="Удаление право для ролей по уникальному идентификатору",
        )(self.delete)

    async def create(self,
                     role_id: int = Body(description="Уникальный ID роли"),
                     permission_ids: list[int] = Body(description="Уникальный IDs прав"),
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_ROLE_PERMISSION_VALUE))):
        use_case = CreateRolePermissionCase(db)
        return await use_case.execute(role_id=role_id, permission_ids=permission_ids)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_ROLE_PERMISSION_VALUE))
    ):
        use_case = DeleteRolePermissionCase(db)
        return await use_case.execute(id=id)
