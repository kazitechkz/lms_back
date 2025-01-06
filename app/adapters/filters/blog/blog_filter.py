from fastapi import Query
from sqlalchemy import or_

from app.adapters.filters.base_filter import BaseFilter
from app.entities.blog import BlogModel


class BlogFilter(BaseFilter):
    def __init__(
        self,
        per_page: int = Query(
            default=20, gt=0, example=20, description="Количество элементов на страницу"
        ),
        page: int = Query(default=1, ge=1, example=1, description="Номер страницы"),
        search: str | None = Query(
            default=None,
            max_length=255,
            min_length=3,
            description="Поисковый запрос",
        ),
    ) -> None:
        super().__init__(per_page, page, search)
        self.per_page = per_page
        self.page = page
        self.search = search
        self.model = BlogModel

    def apply(self) -> list:
        filters = []
        if self.search:
            filters.append(
                or_(
                    self.model.title.like(f"%{self.search}%"),
                    self.model.short_description.like(f"%{self.search}%"),
                    self.model.description.like(f"%{self.search}%"),
                    self.model.author.like(f"%{self.search}%")
                )
            )
        return filters
