from fastapi import Query
from sqlalchemy import or_, and_

from app.adapters.filters.base_filter import BaseFilter
from app.entities.test import QuestionModel


class QuestionFilter(BaseFilter):
    def __init__(
            self,
            per_page: int = Query(
                default=20, gt=0, example=20, description="Количество элементов на страницу"
            ),
            page: int = Query(default=1, ge=1, example=1, description="Номер страницы"),
            test_id: int | None = Query(default=None, ge=1, example=1, description="Test ID"),
            search: str | None = Query(
                default=None,
                max_length=255,
                min_length=3,
                description="Поисковый запрос по наименованию вопроса",
            ),
    ) -> None:
        super().__init__(per_page, page, search)
        self.per_page = per_page
        self.page = page
        self.search = search
        self.model = QuestionModel
        self.test_id = test_id

    def apply(self) -> list:
        filters = []
        if self.search:
            filters.append(
                or_(
                    self.model.text.like(f"%{self.search}%"),
                    self.model.hint.like(f"%{self.search}%"),
                    self.model.explanation.like(f"%{self.search}%")
                )
            )
        if self.test_id:
            filters.append(
                and_(self.model.test_id == self.test_id)
            )
        return filters