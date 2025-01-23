from fastapi import Query
from sqlalchemy import or_, and_

from app.adapters.filters.base_filter import BaseFilter
from app.entities.test import TestModel


class TestFilter(BaseFilter):
    def __init__(
            self,
            per_page: int = Query(
                default=20, gt=0, example=20, description="Количество элементов на страницу"
            ),
            page: int = Query(default=1, ge=1, example=1, description="Номер страницы"),
            course_id: int | None = Query(default=None, ge=1, example=1, description="Course ID"),
            video_id: int | None = Query(default=None, ge=1, example=1, description="Video ID"),
            organization_id: int | None = Query(default=None, ge=1, example=1, description="Organization ID"),
            search: str | None = Query(
                default=None,
                max_length=255,
                min_length=3,
                description="Поисковый запрос по наименованию видеокурса",
            ),
    ) -> None:
        super().__init__(per_page, page, search)
        self.per_page = per_page
        self.page = page
        self.search = search
        self.course_id = course_id
        self.video_id = video_id
        self.organization_id = organization_id
        self.model = TestModel

    def apply(self) -> list:
        filters = []
        if self.search:
            or_(
                self.model.title.like(f"%{self.search}%"),
                self.model.description.like(f"%{self.search}%")
            )
        if self.course_id is not None:
            filters.append(
                    and_(self.model.course_id == self.course_id)
                )
        if self.video_id:
            filters.append(
                and_(self.model.video_id == self.video_id)
            )
        if self.organization_id:
            filters.append(
                and_(self.model.organization_id == self.organization_id)
            )
        return filters
