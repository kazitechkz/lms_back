from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.adapters.dto.language.language_dto import LanguageRDTO
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.use_cases.base_case import BaseUseCase


class AllLanguagesCase(BaseUseCase[List[LanguageRDTO]]):
    def __init__(self, db: AsyncSession):
        self.repository = LanguageRepository(db)

    async def execute(self) -> List[LanguageRDTO]:
        languages = await self.repository.get_all()
        return [LanguageRDTO.from_orm(language) for language in languages]

    async def validate(self):
        pass