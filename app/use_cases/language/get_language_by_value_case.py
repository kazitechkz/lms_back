from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.language.language_dto import LanguageRDTO
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetLanguageByValueCase(BaseUseCase[LanguageRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = LanguageRepository(db)

    async def execute(self, value: str) -> LanguageRDTO:
        model = await self.validate(self.repository, value)
        return LanguageRDTO.from_orm(model)

    async def validate(self, repo: LanguageRepository, value: str):
        filters = [repo.model.value == value]
        model = await repo.get_first_with_filters(filters)
        if not model:
            raise AppExceptionResponse.not_found(message="Локаль не найдена")
        return model
