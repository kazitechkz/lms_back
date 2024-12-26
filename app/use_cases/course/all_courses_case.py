from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.course.course_dto import CourseRDTO
from app.adapters.dto.pagination_dto import Pagination
from app.adapters.filters.course.course_filter import CourseFilter
from app.adapters.repositories.course.course_repository import CourseRepository
from app.entities.course import CourseModel
from app.use_cases.base_case import BaseUseCase


class AllCoursesCase(BaseUseCase[Pagination[CourseRDTO]]):
    def __init__(self, db: AsyncSession, params: CourseFilter):
        self.repository = CourseRepository(db)
        self.params = params

    async def execute(self) -> Pagination[CourseModel]:
        courses = await self.repository.paginate(
            dto=CourseRDTO,
            page=self.params.page,
            per_page=self.params.per_page,
            options=[
                selectinload(self.repository.model.category),
                selectinload(self.repository.model.type)
            ]
        )
        return courses

    async def validate(self):
        pass
