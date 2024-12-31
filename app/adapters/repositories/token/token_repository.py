from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.tokens import TokenModel


class TokenRepository(BaseRepository[TokenModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(TokenModel, db)
