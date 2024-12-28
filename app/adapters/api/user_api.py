from typing import Optional

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.pagination_dto import PaginationUsers
from app.adapters.dto.user.user_dto import UserRDTOWithRelated, UserCDTO
from app.adapters.filters.users.user_filter import UserFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.user.all_users_case import AllUsersCase
from app.use_cases.user.create_user_case import CreateUserCase
from app.use_cases.user.delete_user_case import DeleteUserCase
from app.use_cases.user.get_user_case import GetUserCase
from app.use_cases.user.update_user_case import UpdateUserCase


class UserApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=PaginationUsers,
            summary="Список пользователей",
            description="Получение списка пользователей",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=UserRDTOWithRelated,
            summary="Получить пользователя по уникальному ID",
            description="Получение роли по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=UserRDTOWithRelated,
            summary="Создать пользователя",
            description="Создание пользователя",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=UserRDTOWithRelated,
            summary="Обновить пользователя по уникальному ID",
            description="Обновление пользователя по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалите пользователя по уникальному ID",
            description="Удаление пользователя по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, params: UserFilter = Depends(), db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_USER_VALUE))):
        use_case = AllUsersCase(db)
        return await use_case.execute(params=params)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_USER_VALUE))):
        use_case = GetUserCase(db)
        return await use_case.execute(user_id=id)

    async def create(self, dto: UserCDTO = Depends(), db: AsyncSession = Depends(get_db),
                     file: UploadFile | None = File(default=None, description="Ава"),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_USER_VALUE))):
        use_case = CreateUserCase(db)
        return await use_case.execute(dto=dto, file=file, userDTO=user)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: UserCDTO = Depends(),
        db: AsyncSession = Depends(get_db),
        file: Optional[UploadFile] = File(default=None, description="Ава"),
        user=Depends(permission_dependency(PermissionConstants.UPDATE_USER_VALUE))
    ):
        use_case = UpdateUserCase(db)
        return await use_case.execute(id=id, dto=dto, file=file, userDTO=user)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_USER_VALUE))
    ):
        use_case = DeleteUserCase(db)
        return await use_case.execute(id=id)
