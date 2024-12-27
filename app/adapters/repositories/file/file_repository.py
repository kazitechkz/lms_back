from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities import FileModel


class FileRepository(BaseRepository[FileModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(FileModel, db)
