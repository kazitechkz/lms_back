from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload, joinedload

from app.adapters.dto.course.course_dto import CourseRDTO, CourseRDTOWithRelated
from app.adapters.dto.pagination_dto import PaginationCourse
from app.adapters.filters.course.course_filter import CourseFilter
from app.adapters.repositories.course.course_repository import CourseRepository
from app.entities.course_tag import CourseTagModel
from app.entities.tag import TagModel
from app.use_cases.base_case import BaseUseCase


class AllCoursesCase(BaseUseCase[PaginationCourse]):
    def __init__(self, db: AsyncSession, params: CourseFilter):
        self.repository = CourseRepository(db)
        self.params = params

    async def execute(self):
        courses = await self.repository.paginate(
            dto=CourseRDTOWithRelated,
            page=self.params.page,
            per_page=self.params.per_page,
            options=[
                selectinload(self.repository.model.category),
                selectinload(self.repository.model.lang),
                selectinload(self.repository.model.type),
                selectinload(self.repository.model.tags).selectinload(CourseTagModel.tag),
            ]
        )

        return courses

    async def validate(self):
        pass
