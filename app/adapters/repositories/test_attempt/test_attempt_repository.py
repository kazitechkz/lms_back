from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.test_attempts import TestAttemptModel


class TestAttemptRepository(BaseRepository[TestAttemptModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(TestAttemptModel, db)

