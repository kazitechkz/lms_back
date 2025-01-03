from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.course_material import CourseMaterialModel


class CourseMaterialRepository(BaseRepository[CourseMaterialModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(CourseMaterialModel, db)
