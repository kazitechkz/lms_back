from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_material.course_material_dto import CourseMaterialCDTO, \
    CourseMaterialRDTO
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.course_material.create_course_material_case import CreateCourseMaterialCase
from app.use_cases.course_material.delete_course_material_case import DeleteCourseMaterialCase
from app.use_cases.course_material.get_course_material_case import GetCourseMaterialCase
from app.use_cases.course_material.update_course_material_case import UpdateCourseMaterialCase


class CourseMaterialApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.post(
            "/get/{id}",
            response_model=CourseMaterialRDTO,
            summary="Получить материал курса по ID",
            description="Получение материала курса по ID",
        )(self.get)
        self.router.post(
            "/create",
            response_model=CourseMaterialRDTO,
            summary="Создать материал курса",
            description="Создание материала курса",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=CourseMaterialRDTO,
            summary="Обновить материал курса",
            description="Обновление материала курса",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить материал курса по уникальному ID",
            description="Удаление материала курса по уникальному идентификатору",
        )(self.delete)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_COURSE_MATERIAL_VALUE))):
        use_case = GetCourseMaterialCase(db)
        return await use_case.execute(course_material_id=id)

    async def create(self, dto: CourseMaterialCDTO,
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_COURSE_MATERIAL_VALUE))):
        use_case = CreateCourseMaterialCase(db)
        return await use_case.execute(dto=dto)

    async def update(self, id: PathConstants.IDPath, dto: CourseMaterialCDTO,
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.UPDATE_COURSE_MATERIAL_VALUE))):
        use_case = UpdateCourseMaterialCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
            self,
            id: PathConstants.IDPath,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_COURSE_MATERIAL_VALUE))
    ):
        use_case = DeleteCourseMaterialCase(db)
        return await use_case.execute(id=id)
