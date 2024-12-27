from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleCDTO, RoleRDTO
from app.core.auth_core import get_current_user
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.role.all_roles_case import AllRolesCase
from app.use_cases.role.create_role_case import CreateRoleCase
from app.use_cases.role.delete_role_case import DeleteRoleCase
from app.use_cases.role.get_role_by_value_case import GetRoleByValueCase
from app.use_cases.role.get_role_case import GetRoleCase
from app.use_cases.role.update_role_case import UpdateRoleCase


class RoleApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[RoleRDTO],
            summary="Список ролей",
            description="Получение списка ролей",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=RoleRDTO,
            summary="Получить роль по уникальному ID",
            description="Получение роли по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=RoleRDTO,
            summary="Получить роль по уникальному значению",
            description="Получение роли по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=RoleRDTO,
            summary="Создать роль",
            description="Создание роли",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=RoleRDTO,
            summary="Обновить роль по уникальному ID",
            description="Обновление роли по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалите роль по уникальному ID",
            description="Удаление роли по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
        use_case = AllRolesCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db)):
        use_case = GetRoleCase(db)
        return await use_case.execute(role_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db)
    ):
        use_case = GetRoleByValueCase(db)
        return await use_case.execute(role_value=value)

    async def create(self, dto: RoleCDTO, db: AsyncSession = Depends(get_db)):
        use_case = CreateRoleCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: RoleCDTO,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = UpdateRoleCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = DeleteRoleCase(db)
        return await use_case.execute(id=id)
