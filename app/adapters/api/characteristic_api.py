from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.characteristic.characteristic_dto import CharacteristicRDTO, CharacteristicCDTO
from app.adapters.dto.pagination_dto import PaginationCharacteristics
from app.adapters.filters.characteristic.characteristic_filter import CharacteristicFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.characteristic.all_characteristics_case import AllCharacteristicsCase
from app.use_cases.characteristic.create_characteristic_case import CreateCharacteristicCase
from app.use_cases.characteristic.delete_characteristic_case import DeleteCharacteristicCase
from app.use_cases.characteristic.get_characteristic_by_value_case import GetCharacteristicByValueCase
from app.use_cases.characteristic.get_characteristic_case import GetCharacteristicCase
from app.use_cases.characteristic.update_characteristic_case import UpdateCharacteristicCase


class CharacteristicApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=PaginationCharacteristics,
            summary="Список характеристик",
            description="Получение списка характеристики",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=CharacteristicRDTO,
            summary="Получить характеристику по уникальному ID",
            description="Получение характеристики по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=CharacteristicRDTO,
            summary="Получить характеристику по уникальному значению",
            description="Получение характеристики по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=CharacteristicRDTO,
            summary="Создать характеристику",
            description="Создание характеристики",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=CharacteristicRDTO,
            summary="Обновить характеристику по уникальному ID",
            description="Обновление характеристики по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить характеристику по уникальному ID",
            description="Удаление характеристики по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      params: CharacteristicFilter = Depends(),
                      user=Depends(permission_dependency(PermissionConstants.READ_CHARACTERISTIC_VALUE))):
        use_case = AllCharacteristicsCase(db)
        return await use_case.execute(params)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_CHARACTERISTIC_VALUE))):
        use_case = GetCharacteristicCase(db)
        return await use_case.execute(characteristic_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.READ_CHARACTERISTIC_VALUE))
    ):
        use_case = GetCharacteristicByValueCase(db)
        return await use_case.execute(characteristic_value=value)

    async def create(self, dto: CharacteristicCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_CHARACTERISTIC_VALUE))):
        use_case = CreateCharacteristicCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: CharacteristicCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_CHARACTERISTIC_VALUE))
    ):
        use_case = UpdateCharacteristicCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_CHARACTERISTIC_VALUE))
    ):
        use_case = DeleteCharacteristicCase(db)
        return await use_case.execute(id=id)
