from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.pagination_dto import PaginationTests
from app.adapters.dto.test.test_dto import TestRDTO, TestCDTO, TestUDTO
from app.adapters.filters.test.test_filter import TestFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.test.all_test_case import AllTestsCase
from app.use_cases.test.create_test_case import CreateTestCase
from app.use_cases.test.delete_test_case import DeleteTestCase
from app.use_cases.test.get_test_case import GetTestCase
from app.use_cases.test.update_test_case import UpdateTestCase


class TestApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        pass
        self.router.get(
            "/",
            response_model=PaginationTests,
            summary="Список тестов",
            description="Получение списка тестов",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=TestRDTO,
            summary="Получить тест по уникальному ID",
            description="Получение теста по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=TestRDTO,
            summary="Создать тест",
            description="Создание теста",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=TestRDTO,
            summary="Обновить тест по уникальному ID",
            description="Обновление теста по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить тест по уникальному ID",
            description="Удаление теста по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db), params: TestFilter = Depends(),
                      user=Depends(permission_dependency(PermissionConstants.READ_TEST_VALUE))):
        use_case = AllTestsCase(db=db)
        return await use_case.execute(params=params)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_TEST_VALUE))):
        use_case = GetTestCase(db)
        return await use_case.execute(test_id=id)

    async def create(self, dto: TestCDTO,
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_TEST_VALUE))):
        use_case = CreateTestCase(db)
        return await use_case.execute(dto=dto)

    async def update(
            self,
            id: PathConstants.IDPath,
            dto: TestUDTO,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_TEST_VALUE))
    ):
        use_case = UpdateTestCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
            self,
            id: PathConstants.IDPath,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_TEST_VALUE))
    ):
        use_case = DeleteTestCase(db)
        return await use_case.execute(id=id)
