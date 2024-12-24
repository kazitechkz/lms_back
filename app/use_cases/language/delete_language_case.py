from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.infrastructure.db_constants import AppDbValueConstants
from app.use_cases.base_case import BaseUseCase


class DeleteLanguageCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = LanguageRepository(db)

    async def execute(self, id: int) -> bool:
        await self.validate(repository=self.repository, id=id)
        data = await self.repository.delete(id=id)
        return data

    async def validate(self, repository: LanguageRepository, id: int):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Локаль не найдена")
        if existed.value in AppDbValueConstants.IMMUTABLE_LANGUAGES:
            raise AppExceptionResponse.bad_request(message="Такую локаль нельзя удалять")
