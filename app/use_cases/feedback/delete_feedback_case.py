from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.feedback.feedback_repository import FeedbackRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class DeleteFeedbackCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = FeedbackRepository(db)

    async def execute(self, id: int) -> bool:
        await self.validate(id=id)
        data = await self.repository.delete(id=id)
        return data

    async def validate(self, id: int):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Обращение не найдено")
