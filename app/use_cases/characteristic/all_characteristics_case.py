from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.characteristic.characteristic_dto import CharacteristicRDTO
from app.adapters.dto.pagination_dto import PaginationCharacteristics
from app.adapters.filters.characteristic.characteristic_filter import CharacteristicFilter
from app.adapters.repositories.characteristic.characteristic_repository import CharacteristicRepository
from app.use_cases.base_case import BaseUseCase


class AllCharacteristicsCase(BaseUseCase[PaginationCharacteristics]):
    def __init__(self, db: AsyncSession):
        self.repository = CharacteristicRepository(db)

    async def execute(self, params: CharacteristicFilter):
        characteristics = await self.repository.paginate(
            dto=CharacteristicRDTO,
            page=params.page,
            per_page=params.per_page,
            filters=params.apply()
        )
        return characteristics

    async def validate(self):
        pass
