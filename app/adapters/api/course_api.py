from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course.course_dto import CourseCDTO, CourseRDTOWithRelated
from app.adapters.dto.pagination_dto import PaginationCourse
from app.adapters.filters.course.course_filter import CourseFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.course.all_courses_case import AllCoursesCase
from app.use_cases.course.create_course_case import CreateCourseCase
from app.use_cases.course.delete_course_case import DeleteCourseCase
from app.use_cases.course.get_course_case import GetCourseCase
from app.use_cases.course.update_course_case import UpdateCourseCase


def parse_dto_from_form(title: str = Form(...),
                        short_description: str | None = Form(None),
                        description: str = Form(...),
                        learned: str = Form(...),
                        author: str | None = Form(None),
                        price: int = Form(...),
                        category_id: int = Form(...),
                        type_id: int = Form(...),
                        lang_id: int = Form(...),
                        ) -> CourseCDTO:
    return CourseCDTO(
        title=title,
        description=description,
        short_description=short_description,
        learned=learned,
        author=author,
        price=price,
        category_id=category_id,
        type_id=type_id,
        lang_id=lang_id,
    )


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
            response_model=CourseRDTOWithRelated,
            summary="Получить курс по уникальному ID",
            description="Получение курса по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=CourseRDTOWithRelated,
            summary="Создать курс",
            description="Создание курса",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=CourseRDTOWithRelated,
            summary="Обновить курс по уникальному ID",
            description="Обновление курса по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить курс по уникальному ID",
            description="Удаление курса по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db), params: CourseFilter = Depends(),
                      user=Depends(permission_dependency(PermissionConstants.READ_COURSE_VALUE))):
        use_case = AllCoursesCase(db=db, params=params)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_COURSE_VALUE))):
        use_case = GetCourseCase(db)
        return await use_case.execute(course_id=id)

    async def create(self, dto: CourseCDTO = Depends(parse_dto_from_form),
                     db: AsyncSession = Depends(get_db),
                     thumbnail: UploadFile | None = File(default=None, description="Обложка курса"),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_COURSE_VALUE))):
        use_case = CreateCourseCase(db)
        return await use_case.execute(dto=dto, file=thumbnail)

    async def update(
            self,
            id: PathConstants.IDPath,
            dto: CourseCDTO = Depends(parse_dto_from_form),
            thumbnail: UploadFile | None = File(default=None, description="Обложка курса"),
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_COURSE_VALUE))
    ):
        use_case = UpdateCourseCase(db)
        return await use_case.execute(id=id, dto=dto, file=thumbnail)

    async def delete(
            self,
            id: PathConstants.IDPath,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_COURSE_VALUE))
    ):
        use_case = DeleteCourseCase(db)
        return await use_case.execute(id=id)
