from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase


class TagApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[TagRDTO],
            summary="Список ролей",
            description="Получение списка ролей",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=TagRDTO,
            summary="Получить роль по уникальному ID",
            description="Получение роли по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=TagRDTO,
            summary="Получить роль по уникальному значению",
            description="Получение роли по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=TagRDTO,
            summary="Создать роль",
            description="Создание роли",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=TagRDTO,
            summary="Обновить роль по уникальному ID",
            description="Обновление роли по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалите роль по уникальному ID",
            description="Удаление роли по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db)):
        use_case = AllTagsCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db)):
        use_case = GetTagCase(db)
        return await use_case.execute(tag_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db)
    ):
        use_case = GetTagByValueCase(db)
        return await use_case.execute(tag_value=value)

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
