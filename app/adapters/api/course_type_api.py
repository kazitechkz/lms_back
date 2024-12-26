from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_type.course_type_dto import CourseTypeRDTO, CourseTypeCDTO
from app.adapters.dto.role.role_dto import RoleCDTO
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.course_type.all_course_type_case import AllCourseTypeCase
from app.use_cases.course_type.create_course_type_case import CreateCourseTypeCase
from app.use_cases.course_type.delete_course_type_case import DeleteCourseTypeCase
from app.use_cases.course_type.get_course_type_by_value_case import GetCourseTypeByValueCase
from app.use_cases.course_type.get_course_type_case import GetCourseTypeCase
from app.use_cases.course_type.update_course_type_case import UpdateCourseTypeCase


class CourseTypeApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[CourseTypeRDTO],
            summary="Список типов курсов",
            description="Получение списка типов курсов",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=CourseTypeRDTO,
            summary="Получить тип курса по уникальному ID",
            description="Получение типа курса по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=CourseTypeRDTO,
            summary="Получить тип курса по уникальному значению",
            description="Получение типа курса по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=CourseTypeRDTO,
            summary="Создать тип курса",
            description="Создание типа курса",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=CourseTypeRDTO,
            summary="Обновить тип курса по уникальному ID",
            description="Обновление типа курса по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить тип курса по уникальному ID",
            description="Удаление типа курса по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db)):
        use_case = AllCourseTypeCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db)):
        use_case = GetCourseTypeCase(db)
        return await use_case.execute(role_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db)
    ):
        use_case = GetCourseTypeByValueCase(db)
        return await use_case.execute(role_value=value)

    async def create(self, dto: CourseTypeCDTO, db: AsyncSession = Depends(get_db)):
        use_case = CreateCourseTypeCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: CourseTypeCDTO,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = UpdateCourseTypeCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = DeleteCourseTypeCase(db)
        return await use_case.execute(id=id)
