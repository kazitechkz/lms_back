from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.feedback.feedback_dto import FeedbackRDTOWithRelated
from app.adapters.dto.pagination_dto import PaginationFeedbacks
from app.adapters.filters.feedback.feedback_filter import FeedbackFilter
from app.adapters.repositories.feedback.feedback_repository import FeedbackRepository
from app.use_cases.base_case import BaseUseCase


class AllFeedbacksCase(BaseUseCase[PaginationFeedbacks]):
    def __init__(self, db: AsyncSession):
        self.repository = FeedbackRepository(db)

    async def execute(self, params: FeedbackFilter):
        feedbacks = await self.repository.paginate(
            dto=FeedbackRDTOWithRelated,
            page=params.page,
            per_page=params.per_page,
            filters=params.apply(),
            options=[
                joinedload(self.repository.model.test),
                joinedload(self.repository.model.question)
            ]
        )
        return feedbacks

    async def validate(self):
        pass
