from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.video_material import VideoMaterialModel


class VideoMaterialRepository(BaseRepository[VideoMaterialModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(VideoMaterialModel, db)
