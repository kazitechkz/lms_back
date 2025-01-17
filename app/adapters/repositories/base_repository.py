from typing import Any, Generic, List, Optional, TypeVar

from pydantic import BaseModel
from sqlalchemy import func, select, delete
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.pagination_dto import Pagination
from app.core.app_exception_response import AppExceptionResponse

T = TypeVar("T")


class BaseRepository(Generic[T]):
    """Базовый репозиторий для CRUD-операций."""

    def __init__(self, model: type[T], db: AsyncSession) -> None:
        self.model = model
        self.db = db

    async def get(self, id: int, options: Optional[List[Any]] = None) -> Optional[T]:
        """Получение объекта по ID."""
        query = select(self.model).filter(self.model.id == id)
        if options:
            query = query.options(*options)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def get_many(self, ids: list[int]):
        """
        Получить записи по списку идентификаторов.

        :param ids: Список идентификаторов записей.
        :return: Список объектов модели.
        """
        if not ids:
            return []

        query = select(self.model).where(self.model.id.in_(ids))
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_all(self, options: Optional[List[Any]] = None) -> List[T]:
        """Получение всех объектов."""
        query = select(self.model)
        if options:
            query = query.options(*options)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_with_filters(
        self, filters: List[Any], options: Optional[List[Any]] = None
    ) -> List[T]:
        """Получение объектов с фильтрацией."""
        query = select(self.model).filter(*filters)
        if options:
            query = query.options(*options)
        result = await self.db.execute(query)
        return result.scalars().all()

    async def get_first_with_filters(
        self, filters: List[Any], options: Optional[List[Any]] = None
    ) -> Optional[T]:
        """Получение первого объекта с фильтрацией."""
        query = select(self.model).filter(*filters)
        if options:
            query = query.options(*options)
        result = await self.db.execute(query)
        return result.scalars().first()

    async def paginate(
        self,
        dto: BaseModel,
        page: int = 1,
        per_page: int = 20,
        filters: Optional[List[Any]] = None,
        options: Optional[List[Any]] = None,
    ) -> Pagination:
        """Пагинация объектов с фильтрацией."""
        query = select(self.model)
        if filters:
            query = query.filter(*filters)
        if options:
            query = query.options(*options)

        # Подсчёт общего количества элементов
        total_items = await self.db.scalar(
            select(func.count()).select_from(query.subquery())
        )
        total_pages = (total_items + per_page - 1) // per_page

        # Элементы текущей страницы
        results = await self.db.execute(
            query.limit(per_page).offset((page - 1) * per_page)
        )
        items = results.scalars().all()

        # Преобразование в DTO
        dto_items = [dto.from_orm(item) for item in items]
        return Pagination(
            items=dto_items,
            per_page=per_page,
            page=page,
            total_pages=total_pages,
            total_items=total_items,
        )

    async def create(self, obj: T, options: Optional[List[Any]] = None) -> T:
        """Создание объекта."""
        try:
            self.db.add(obj)
            await self.db.commit()
            # Если переданы опции, подгружаем связанные данные
            if options:
                query = select(type(obj)).options(*options).filter_by(id=obj.id)
                result = await self.db.execute(query)
                obj = result.scalar_one_or_none()
            else:
                await self.db.refresh(obj)
            return obj
        except IntegrityError as e:
            await self.db.rollback()
            raise AppExceptionResponse.internal_error(message=self._parse_integrity_error(e))

    async def create_many(self, objs: list):
        """
        Массовое создание записей.

        :param objs: Список объектов модели.
        :return: Список созданных объектов.
        """
        if not objs:
            return []

        # Добавляем все объекты в сессию
        self.db.add_all(objs)

        # Фиксируем изменения в базе данных
        await self.db.commit()

        # Обновляем объекты с возвращёнными ID (если есть автоинкремент)
        for obj in objs:
            await self.db.refresh(obj)

        return objs

    async def update(self, obj: T, dto: BaseModel, options: Optional[List[Any]] = None) -> T:
        """Обновление объекта."""
        try:
            # Обновляем только те поля, которые заданы в DTO
            for field, value in dto.dict(exclude_unset=True).items():
                if hasattr(obj, field):
                    setattr(obj, field, value)

            await self.db.commit()

            # Если переданы опции, подгружаем связанные данные
            if options:
                query = select(type(obj)).options(*options).filter_by(id=obj.id)
                result = await self.db.execute(query)
                obj = result.scalar_one_or_none()
            else:
                await self.db.refresh(obj)

            return obj
        except IntegrityError as e:
            await self.db.rollback()
            raise AppExceptionResponse.internal_error(message=self._parse_integrity_error(e))

    async def delete(self, id: int) -> bool:
        """Удаление объекта через execute."""
        obj = await self.get(id)
        if not obj:
            raise AppExceptionResponse.not_found(message="Не найдено")

        # Удаляем объект через SQL-запрос
        await self.db.execute(
            delete(self.model).where(self.model.id == id)
        )
        await self.db.commit()

        # Проверяем, что объект больше не существует
        deleted_obj = await self.get(id)
        return deleted_obj is None

    async def delete_with_ids(self, ids: list[int]):
        await self.db.execute(
            delete(self.model).where(self.model.id.in_(ids))
        )
        await self.db.commit()

    async def delete_with_filters(self, filters: list):
        await self.db.execute(
            delete(self.model).where(*filters)
        )
        await self.db.commit()

    def _parse_integrity_error(self, error: IntegrityError) -> str:
        """Парсинг ошибок уникальности."""
        orig_msg = str(error.orig)
        return f"IntegrityError: {orig_msg.split(':')[-1].strip()}"
