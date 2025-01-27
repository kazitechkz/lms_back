from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.question_type import QuestionTypeModel


class QuestionTypeRepository(BaseRepository[QuestionTypeModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(QuestionTypeModel, db)
