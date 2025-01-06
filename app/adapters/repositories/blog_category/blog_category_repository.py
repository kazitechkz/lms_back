from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.blog_category import BlogCategoryModel


class BlogCategoryRepository(BaseRepository[BlogCategoryModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(BlogCategoryModel, db)
