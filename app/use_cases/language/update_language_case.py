from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.language.language_dto import LanguageRDTO, LanguageCDTO
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateLanguageCase(BaseUseCase[LanguageRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = LanguageRepository(db)

    async def execute(self, id: int, dto: LanguageCDTO) -> LanguageRDTO:
        obj = await self.validate(repository=self.repository, id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return LanguageRDTO.from_orm(data)

    async def validate(self, repository: LanguageRepository, id: int, dto: LanguageCDTO):
        existed = await repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Локаль не найдена")
        if await repository.get_first_with_filters(
            [repository.model.value == dto.value, repository.model.id != id]
        ):
            raise AppExceptionResponse.bad_request(
                "Локаль с таким значением уже существует"
            )
        return existed
