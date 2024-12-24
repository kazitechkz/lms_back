from sqlalchemy.ext.asyncio import AsyncSession
from app.adapters.dto.language.language_dto import LanguageRDTO, LanguageCDTO
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateLanguageCase(BaseUseCase[LanguageRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = LanguageRepository(db)

    async def execute(self, dto: LanguageCDTO) -> LanguageRDTO:
        obj = await self.validate(repository=self.repository, dto=dto)
        data = await self.repository.create(obj=obj)
        return LanguageRDTO.from_orm(data)

    async def validate(self, repository: LanguageRepository, dto: LanguageCDTO):
        if await repository.get_first_with_filters(
            [repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Локаль с таким значением уже существует"
            )
        return self.repository.model(**dto.dict())