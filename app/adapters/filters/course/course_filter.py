from fastapi import Query
from sqlalchemy import or_, and_

from app.adapters.filters.base_filter import BaseFilter
from app.entities.course import CourseModel


class CourseFilter(BaseFilter):
    def __init__(
        self,
        per_page: int = Query(
            default=20, gt=0, example=20, description="Количество элементов на страницу"
        ),
        page: int = Query(default=1, ge=1, example=1, description="Номер страницы"),
        type_id: int | None = Query(default=None, example=1, description="ID типа"),
        category_id: int | None = Query(default=None, example=1, description="ID категории"),
        lang_id: int | None = Query(default=None, example=1, description="ID языка"),
        search: str | None = Query(
            default=None,
            max_length=255,
            min_length=3,
            description="Поисковый запрос по наименованию курса",
        ),
    ) -> None:
        super().__init__(per_page, page, search)
        self.per_page = per_page
        self.page = page
        self.search = search
        self.category_id = category_id
        self.lang_id = lang_id
        self.type_id = type_id
        self.model = CourseModel

    def apply(self) -> list:
        filters = []
        if self.search:
            filters.append(
                or_(
                    self.model.title.like(f"%{self.search}%"),
                    self.model.author.like(f"%{self.search}%")
                )
            )
        if self.category_id:
            filters.append(
                and_(self.model.category_id == self.category_id)
            )
        if self.lang_id:
            filters.append(
                and_(self.model.lang_id == self.lang_id)
            )
        if self.type_id:
            filters.append(
                and_(self.model.type_id == self.type_id)
            )
        return filters
