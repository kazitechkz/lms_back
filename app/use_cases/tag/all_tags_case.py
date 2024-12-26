from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.tag.tag_dto import TagRDTO
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.use_cases.base_case import BaseUseCase


class AllTagsCase(BaseUseCase[List[TagRDTO]]):
    def __init__(self, db: AsyncSession):
        self.repository = TagRepository(db)

    async def execute(self) -> List[TagRDTO]:
        roles = await self.repository.get_all()
        return [TagRDTO.from_orm(role) for role in roles]

    async def validate(self):
        pass
