from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities import RoleModel
from app.infrastructure.database import get_db


class RoleRepository(BaseRepository[RoleModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(RoleModel, db)
