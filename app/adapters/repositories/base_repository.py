from typing import Any, Generic, List, Optional, TypeVar

from pydantic import BaseModel
from sqlalchemy import func, select
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

    async def create(self, obj: T) -> T:
        """Создание объекта."""
        try:
            self.db.add(obj)
            await self.db.commit()
            await self.db.refresh(obj)
            return obj
        except IntegrityError as e:
            await self.db.rollback()
            raise ValueError(self._parse_integrity_error(e))

    async def update(self, obj: T, data: dict[str, Any]) -> T:
        """Обновление объекта."""
        try:
            for field, value in data.items():
                setattr(obj, field, value)
            await self.db.commit()
            await self.db.refresh(obj)
            return obj
        except IntegrityError as e:
            await self.db.rollback()
            raise ValueError(self._parse_integrity_error(e))

    async def delete(self, id: int) -> None:
        """Удаление объекта."""
        obj = await self.get(id)
        if not obj:
            raise AppExceptionResponse.not_found(message="Не найдено")
        await self.db.delete(obj)
        await self.db.commit()

    def _parse_integrity_error(self, error: IntegrityError) -> str:
        """Парсинг ошибок уникальности."""
        orig_msg = str(error.orig)
        return f"IntegrityError: {orig_msg.split(':')[-1].strip()}"
