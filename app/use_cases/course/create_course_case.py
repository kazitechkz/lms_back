from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateTagCase(BaseUseCase[TagRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = TagRepository(db)

    async def execute(self, dto: TagCDTO) -> TagRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return TagRDTO.from_orm(data)

    async def validate(self, dto: TagCDTO):
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Тег с таким значением уже существует"
            )
        return self.repository.model(**dto.dict())
