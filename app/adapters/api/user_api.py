from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.pagination_dto import PaginationUsers
from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.filters.users.user_filter import UserFilter
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase
from app.use_cases.user.all_users_case import AllUsersCase


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

    async def get_all(self, params: UserFilter = Depends(), db: AsyncSession = Depends(get_db)):
        use_case = AllUsersCase(db)
        return await use_case.execute(params=params)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db)):
        use_case = GetTagCase(db)
        return await use_case.execute(tag_id=id)

    async def create(self, dto: TagCDTO, db: AsyncSession = Depends(get_db)):
        use_case = CreateTagCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: TagCDTO,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = UpdateTagCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = DeleteTagCase(db)
        return await use_case.execute(id=id)
