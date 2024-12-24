from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.language.language_dto import LanguageRDTO
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetLanguageCase(BaseUseCase[LanguageRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = LanguageRepository(db)

    async def execute(self, id: int) -> LanguageRDTO:
        model = await self.repository.get(id)
        if not model:
            raise AppExceptionResponse.not_found()
        return LanguageRDTO.from_orm(model)

    async def validate(self):
        pass
