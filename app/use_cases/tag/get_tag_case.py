from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.dto.tag.tag_dto import TagRDTO
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetTagCase(BaseUseCase[RoleRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = TagRepository(db)

    async def execute(self, tag_id: int) -> TagRDTO:
        tag = await self.validate(tag_id=tag_id)
        return TagRDTO.from_orm(tag)

    async def validate(self, tag_id: int):
        tag = await self.repository.get(tag_id)
        if not tag:
            raise AppExceptionResponse.not_found("Тег не найден")
        return tag
