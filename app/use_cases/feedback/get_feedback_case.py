from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.feedback.feedback_dto import FeedbackRDTOWithRelated
from app.adapters.repositories.feedback.feedback_repository import FeedbackRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetFeedbackCase(BaseUseCase[FeedbackRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = FeedbackRepository(db)

    async def execute(self, feedback_id: int) -> FeedbackRDTOWithRelated:
        feedback = await self.validate(feedback_id=feedback_id)
        return FeedbackRDTOWithRelated.from_orm(feedback)

    async def validate(self, feedback_id: int):
        feedback = await self.repository.get(feedback_id, options=[
            joinedload(self.repository.model.test),
            joinedload(self.repository.model.question)
        ])
        if not feedback:
            raise AppExceptionResponse.not_found("Обращение не найдено")
        return feedback
