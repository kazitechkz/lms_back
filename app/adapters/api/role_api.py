from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleRDTO
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.role.all_roles_case import AllRolesCase
from app.use_cases.role.get_role_by_value_case import GetRoleByValueCase
from app.use_cases.role.get_role_case import GetRoleCase


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

    async def get_all(self, db: AsyncSession = Depends(get_db)):
        """Эндпоинт для получения списка ролей."""
        use_case = AllRolesCase(db)
        return await use_case.execute()

    async def get(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db)
    ):
        use_case = GetRoleCase(db)
        return await use_case.execute(role_id=id)

    async def get_by_value(
        self,
        value: PathConstants.ValuePath,
        db: AsyncSession = Depends(get_db)
    ):
        use_case = GetRoleByValueCase(db)
        return await use_case.execute(role_value=value)
