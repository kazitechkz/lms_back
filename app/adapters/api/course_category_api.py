from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO, CourseCategoryCDTO, \
    CourseCategoryRDTOWithRelated
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.course_category.all_course_category_case import AllCourseCategoryCase
from app.use_cases.course_category.create_course_category_case import CreateCourseCategoryCase
from app.use_cases.course_category.delete_course_category_case import DeleteCourseCategoryCase
from app.use_cases.course_category.get_course_category_by_value_case import GetCourseCategoryByValueCase
from app.use_cases.course_category.get_course_category_case import GetCourseCategoryCase
from app.use_cases.course_category.update_course_category_case import UpdateCourseCategoryCase


class CourseCategoryApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[CourseCategoryRDTOWithRelated],
            summary="Список категории курсов",
            description="Получение списка категории курсов",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=CourseCategoryRDTO,
            summary="Получить категорию по уникальному ID",
            description="Получение категории по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=CourseCategoryRDTO,
            summary="Получить категорию по уникальному значению",
            description="Получение категории по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=CourseCategoryRDTOWithRelated,
            summary="Создать категорию",
            description="Создание категории",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=CourseCategoryRDTOWithRelated,
            summary="Обновить категорию по уникальному ID",
            description="Обновление категории по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалите категорию по уникальному ID",
            description="Удаление категории по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_COURSE_CATEGORY_VALUE))):
        use_case = AllCourseCategoryCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_COURSE_CATEGORY_VALUE))):
        use_case = GetCourseCategoryCase(db)
        return await use_case.execute(course_category_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.READ_COURSE_CATEGORY_VALUE))
    ):
        use_case = GetCourseCategoryByValueCase(db)
        return await use_case.execute(course_category_value=value)

    async def create(self, dto: CourseCategoryCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_COURSE_CATEGORY_VALUE))):
        use_case = CreateCourseCategoryCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: CourseCategoryCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_COURSE_CATEGORY_VALUE))
    ):
        use_case = UpdateCourseCategoryCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        delete_cascade: bool = False,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_COURSE_CATEGORY_VALUE))
    ):
        use_case = DeleteCourseCategoryCase(db)
        return await use_case.execute(id=id, delete_cascade=delete_cascade)
