from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.course_type import CourseTypeModel


class CourseTypeRepository(BaseRepository[CourseTypeModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(CourseTypeModel, db)
