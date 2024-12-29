from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.course_tag import CourseTagModel


class CourseTagRepository(BaseRepository[CourseTagModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(CourseTagModel, db)
