from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.organization import OrganizationModel


class OrganizationRepository(BaseRepository[OrganizationModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(OrganizationModel, db)
