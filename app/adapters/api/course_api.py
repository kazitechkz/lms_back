from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course.course_dto import CourseCDTO, CourseRDTO
from app.adapters.dto.pagination_dto import PaginationCourse
from app.adapters.filters.course.course_filter import CourseFilter
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.course.all_courses_case import AllCoursesCase
from app.use_cases.course.create_course_case import CreateCourseCase
from app.use_cases.course.delete_course_case import DeleteCourseCase
from app.use_cases.course.get_course_case import GetCourseCase
from app.use_cases.course.update_course_case import UpdateCourseCase
from app.use_cases.course_category.get_course_category_case import GetCourseCategoryCase


class CourseApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=PaginationCourse,
            summary="Список курсов",
            description="Получение списка курсов",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=CourseRDTO,
            summary="Получить курс по уникальному ID",
            description="Получение курса по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=bool,
            summary="Создать курс",
            description="Создание курса",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=CourseRDTO,
            summary="Обновить курс по уникальному ID",
            description="Обновление курса по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить курс по уникальному ID",
            description="Удаление курса по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db), params: CourseFilter = Depends()):
        use_case = AllCoursesCase(db=db, params=params)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db)):
        use_case = GetCourseCase(db)
        return await use_case.execute(course_id=id)

    async def create(self, dto: CourseCDTO, db: AsyncSession = Depends(get_db)):
        use_case = CreateCourseCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: CourseCDTO,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = UpdateCourseCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
    ):
        use_case = DeleteCourseCase(db)
        return await use_case.execute(id=id)