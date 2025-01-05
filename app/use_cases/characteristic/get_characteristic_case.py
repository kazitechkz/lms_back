from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.characteristic.characteristic_dto import CharacteristicRDTO
from app.adapters.repositories.characteristic.characteristic_repository import CharacteristicRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetCharacteristicCase(BaseUseCase[CharacteristicRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = CharacteristicRepository(db)

    async def execute(self, characteristic_id: int) -> CharacteristicRDTO:
        characteristic = await self.validate(characteristic_id=characteristic_id)
        return CharacteristicRDTO.from_orm(characteristic)

    async def validate(self, characteristic_id: int):
        characteristic = await self.repository.get(characteristic_id)
        if not characteristic:
            raise AppExceptionResponse.not_found("Характеристика не найдена")
        return characteristic
