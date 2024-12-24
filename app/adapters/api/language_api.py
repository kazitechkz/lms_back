from fastapi import APIRouter, Depends, Path
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.language.language_dto import LanguageRDTO, LanguageCDTO
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.language.all_languages_case import AllLanguagesCase
from app.use_cases.language.create_language_case import CreateLanguageCase
from app.use_cases.language.delete_language_case import DeleteLanguageCase
from app.use_cases.language.get_language_by_value_case import GetLanguageByValueCase
from app.use_cases.language.get_language_case import GetLanguageCase
from app.use_cases.language.update_language_case import UpdateLanguageCase


class LanguageApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[LanguageRDTO],
            summary="Список локалей",
            description="Получение списка локалей",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=LanguageRDTO,
            summary="Получить локаль по уникальному ID",
            description="Получение локали по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=LanguageRDTO,
            summary="Получить локаль по уникальному значению",
            description="Получение локаль по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=LanguageRDTO,
            summary="Создать локаль",
            description="Создание локали",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=LanguageRDTO,
            summary="Обновить локали по уникальному ID",
            description="Обновление локали по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалите локаль по уникальному ID",
            description="Удаление локали по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db)):
        use_case = AllLanguagesCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db)):
        use_case = GetLanguageCase(db)
        return await use_case.execute(id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db)
    ):
        use_case = GetLanguageByValueCase(db)
        return await use_case.execute(value=value)

    async def create(self, dto: LanguageCDTO, db: AsyncSession = Depends(get_db)):
        use_case = CreateLanguageCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: LanguageCDTO,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = UpdateLanguageCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = DeleteLanguageCase(db)
        return await use_case.execute(id=id)
