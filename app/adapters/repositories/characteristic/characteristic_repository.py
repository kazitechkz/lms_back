from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.characteristic import CharacteristicModel


class CharacteristicRepository(BaseRepository[CharacteristicModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(CharacteristicModel, db)
