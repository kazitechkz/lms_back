from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.blog import BlogModel


class BlogRepository(BaseRepository[BlogModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(BlogModel, db)
