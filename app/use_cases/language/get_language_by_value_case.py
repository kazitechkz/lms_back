from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.language.language_dto import LanguageRDTO
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetLanguageByValueCase(BaseUseCase[LanguageRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = LanguageRepository(db)

    async def execute(self, value: str) -> LanguageRDTO:
        filters = [self.repository.model.value == value]
        model = await self.repository.get_first_with_filters(filters)
        if not model:
            raise AppExceptionResponse.not_found()
        return LanguageRDTO.from_orm(model)

    async def validate(self):
        pass
