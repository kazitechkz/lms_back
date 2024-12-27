from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from app.adapters.dto.course.course_dto import CourseRDTO
from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO
from app.adapters.dto.pagination_dto import Pagination, PaginationCourse
from app.adapters.filters.course.course_filter import CourseFilter
from app.adapters.repositories.course.course_repository import CourseRepository
from app.entities import CourseCategoryModel
from app.entities.course import CourseModel
from app.use_cases.base_case import BaseUseCase


class AllCoursesCase(BaseUseCase[PaginationCourse]):
    def __init__(self, db: AsyncSession, params: CourseFilter):
        self.repository = CourseRepository(db)
        self.params = params

    async def execute(self):
        courses = await self.repository.paginate(
            dto=CourseRDTO,
            page=self.params.page,
            per_page=self.params.per_page,
            options=[
                selectinload(self.repository.model.category),
                selectinload(self.repository.model.category),
                joinedload(self.repository.model.type)
            ]
        )

        return courses

    async def validate(self):
        pass
