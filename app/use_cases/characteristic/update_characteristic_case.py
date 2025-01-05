from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.characteristic.characteristic_dto import CharacteristicRDTO, CharacteristicCDTO
from app.adapters.repositories.characteristic.characteristic_repository import CharacteristicRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateCharacteristicCase(BaseUseCase[CharacteristicRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CharacteristicRepository(db)

    async def execute(self, id: int, dto: CharacteristicCDTO) -> CharacteristicRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return CharacteristicRDTO.from_orm(data)

    async def validate(self, id: int, dto: CharacteristicCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Характеристика не найден")
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value, self.repository.model.id != id]
        ):
            raise AppExceptionResponse.bad_request(
                "Характеристика с таким значением уже существует"
            )
        return existed
