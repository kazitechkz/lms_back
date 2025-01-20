from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.dto.test_type.tag_type_dto import TestTypeRDTO, TestTypeCDTO
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase
from app.use_cases.test_type.all_test_types_case import AllTestTypesCase
from app.use_cases.test_type.create_test_type_case import CreateTestTypeCase
from app.use_cases.test_type.delete_test_type_case import DeleteTestTypeCase
from app.use_cases.test_type.get_test_type_by_value_case import GetTestTypeByValueCase
from app.use_cases.test_type.get_test_type_case import GetTestTypeCase
from app.use_cases.test_type.update_test_type_case import UpdateTestTypeCase


class TestTypeApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[TestTypeRDTO],
            summary="Список типов теста",
            description="Получение списка типов теста",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=TestTypeRDTO,
            summary="Получить тип теста по уникальному ID",
            description="Получение типов теста по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=TestTypeRDTO,
            summary="Получить тип теста по уникальному значению",
            description="Получение типов теста по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=TestTypeRDTO,
            summary="Создать тип теста",
            description="Создание типов теста",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=TestTypeRDTO,
            summary="Обновить тип теста по уникальному ID",
            description="Обновление типов теста по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить тип теста по уникальному ID",
            description="Удаление типов теста по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))):
        use_case = AllTestTypesCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))):
        use_case = GetTestTypeCase(db)
        return await use_case.execute(test_type_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))
    ):
        use_case = GetTestTypeByValueCase(db)
        return await use_case.execute(test_type_value=value)

    async def create(self, dto: TestTypeCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_ROLE_VALUE))):
        use_case = CreateTestTypeCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: TestTypeCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_ROLE_VALUE))
    ):
        use_case = UpdateTestTypeCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_ROLE_VALUE))
    ):
        use_case = DeleteTestTypeCase(db)
        return await use_case.execute(id=id)
