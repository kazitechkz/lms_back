from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.tag.tag_dto import TagRDTO
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetTagByValueCase(BaseUseCase[TagRDTO]):
    def __init__(self, db: AsyncSession):
        self.tag_repository = TagRepository(db)

    async def execute(self, tag_value: str) -> TagRDTO:
        tag = await self.validate(tag_value=tag_value)
        return TagRDTO.from_orm(tag)

    async def validate(self, tag_value: str):
        filters = [self.tag_repository.model.value == tag_value]
        tag = await self.tag_repository.get_first_with_filters(filters)
        if not tag:
            raise AppExceptionResponse.not_found("Тег не найден")
        return tag
