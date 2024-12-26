from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.course import CourseModel


class CourseRepository(BaseRepository[CourseModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(CourseModel, db)
