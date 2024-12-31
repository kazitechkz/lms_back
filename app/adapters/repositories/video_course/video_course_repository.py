from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.video_courses import VideoCourseModel


class VideoCourseRepository(BaseRepository[VideoCourseModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(VideoCourseModel, db)
