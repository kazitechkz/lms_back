from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.tag.tag_dto import TagCDTO, TagRDTO
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateTagCase(BaseUseCase[TagRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = TagRepository(db)

    async def execute(self, id: int, dto: TagCDTO) -> TagRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return TagRDTO.from_orm(data)

    async def validate(self, id: int, dto: TagCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Тег не найден")
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value, self.repository.model.id != id]
        ):
            raise AppExceptionResponse.bad_request(
                "Тег с таким значением уже существует"
            )
        return existed
