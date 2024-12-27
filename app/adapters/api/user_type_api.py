from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.dto.user_type.user_type_dto import UserTypeRDTO
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase
from app.use_cases.user_type.all_user_type_case import AllUserTypeCase
from app.use_cases.user_type.get_user_type_by_value_case import GetUserTypeByValueCase
from app.use_cases.user_type.get_user_type_case import GetUserTypeCase


class UserTypeApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[UserTypeRDTO],
            summary="Список типов пользователей",
            description="Получение списка типов пользователей",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=UserTypeRDTO,
            summary="Получить тип пользователя по уникальному ID",
            description="Получение типа пользователя по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=UserTypeRDTO,
            summary="Получить тип пользователя по уникальному значению",
            description="Получение типа пользователя по уникальному значению",
        )(self.get_by_value)

    async def get_all(self, db: AsyncSession = Depends(get_db)):
        use_case = AllUserTypeCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db)):
        use_case = GetUserTypeCase(db)
        return await use_case.execute(user_type_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db)
    ):
        use_case = GetUserTypeByValueCase(db)
        return await use_case.execute(user_type_value=value)
