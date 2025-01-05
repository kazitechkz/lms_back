from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.characteristic.characteristic_dto import CharacteristicRDTO, CharacteristicCDTO
from app.adapters.repositories.characteristic.characteristic_repository import CharacteristicRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateCharacteristicCase(BaseUseCase[CharacteristicRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CharacteristicRepository(db)

    async def execute(self, dto: CharacteristicCDTO) -> CharacteristicRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return CharacteristicRDTO.from_orm(data)

    async def validate(self, dto: CharacteristicCDTO):
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Характеристика с таким значением уже существует"
            )
        return self.repository.model(**dto.dict())
