from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.characteristic.characteristic_dto import CharacteristicRDTO
from app.adapters.repositories.characteristic.characteristic_repository import CharacteristicRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetCharacteristicByValueCase(BaseUseCase[CharacteristicRDTO]):
    def __init__(self, db: AsyncSession):
        self.characteristic_repository = CharacteristicRepository(db)

    async def execute(self, characteristic_value: str) -> CharacteristicRDTO:
        characteristic = await self.validate(characteristic_value=characteristic_value)
        return CharacteristicRDTO.from_orm(characteristic)

    async def validate(self, characteristic_value: str):
        filters = [self.characteristic_repository.model.value == characteristic_value]
        characteristic = await self.characteristic_repository.get_first_with_filters(filters)
        if not characteristic:
            raise AppExceptionResponse.not_found("Характеристика не найдена")
        return characteristic
