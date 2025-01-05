from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.test import TestModel


class TestRepository(BaseRepository[TestModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(TestModel, db)
