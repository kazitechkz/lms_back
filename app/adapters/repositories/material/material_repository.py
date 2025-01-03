from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.material import MaterialModel


class MaterialRepository(BaseRepository[MaterialModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(MaterialModel, db)
