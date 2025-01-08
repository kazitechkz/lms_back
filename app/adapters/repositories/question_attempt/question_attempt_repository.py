from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.question_attempts import QuestionAttemptModel


class QuestionAttemptRepository(BaseRepository[QuestionAttemptModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(QuestionAttemptModel, db)

