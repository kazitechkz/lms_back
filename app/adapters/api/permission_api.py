from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.permission.permission_dto import PermissionRDTO, PermissionCDTO
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.permission.all_permission_case import AllPermissionCase
from app.use_cases.permission.create_permission_case import CreatePermissionCase
from app.use_cases.permission.delete_permission_case import DeletePermissionCase
from app.use_cases.permission.get_permission_by_value_case import GetPermissionByValueCase
from app.use_cases.permission.get_permission_case import GetPermissionCase
from app.use_cases.permission.update_permission_case import UpdatePermissionCase


class PermissionApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[PermissionRDTO],
            summary="Список прав",
            description="Получение списка прав",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=PermissionRDTO,
            summary="Получить право по уникальному ID",
            description="Получение прав по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=PermissionRDTO,
            summary="Получить право по уникальному значению",
            description="Получение прав по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=PermissionRDTO,
            summary="Создать право",
            description="Создание прав",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=PermissionRDTO,
            summary="Обновить право по уникальному ID",
            description="Обновление право по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалите право по уникальному ID",
            description="Удаление право по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_PERMISSION_VALUE))):
        use_case = AllPermissionCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_PERMISSION_VALUE))):
        use_case = GetPermissionCase(db)
        return await use_case.execute(permission_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.READ_PERMISSION_VALUE))
    ):
        use_case = GetPermissionByValueCase(db)
        return await use_case.execute(permission_value=value)

    async def create(self, dto: PermissionCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_PERMISSION_VALUE))):
        use_case = CreatePermissionCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: PermissionCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_PERMISSION_VALUE))
    ):
        use_case = UpdatePermissionCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_PERMISSION_VALUE))
    ):
        use_case = DeletePermissionCase(db)
        return await use_case.execute(id=id)
