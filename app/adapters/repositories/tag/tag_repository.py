from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.base_repository import BaseRepository
from app.entities.tag import TagModel


class TagRepository(BaseRepository[TagModel]):
    def __init__(self, db: AsyncSession) -> None:
        super().__init__(TagModel, db)

    async def get_all_by_ids(self, ids: list[int]):
        res = await self.db.execute(
            select(TagModel).where(TagModel.id.in_(ids))
        )
        return res.scalars().all()
