from fastapi import Query
from sqlalchemy import or_, and_

from app.adapters.filters.base_filter import BaseFilter
from app.entities.video_courses import VideoCourseModel


class VideoCourseFilter(BaseFilter):
    def __init__(
            self,
            per_page: int = Query(
                default=20, gt=0, example=20, description="Количество элементов на страницу"
            ),
            page: int = Query(default=1, ge=1, example=1, description="Номер страницы"),
            course_id: int | None = Query(default=None, example=1, description="ID course"),
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
        self.model = VideoCourseModel

    def apply(self) -> list:
        filters = []
        if self.search:
            filters.append(
                or_(
                    self.model.title.like(f"%{self.search}%"),
                    self.model.description.like(f"%{self.search}%")
                )
            )
        if self.course_id:
            filters.append(
                    and_(self.model.course_id == self.course_id)
                )
        return filters
