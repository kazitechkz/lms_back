from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.feedback import FeedbackModel


class FeedbackRepository(BaseRepository[FeedbackModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(FeedbackModel, db)
