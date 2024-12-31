from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.pagination_dto import PaginationVideoCourses
from app.adapters.dto.video_course.video_course_dto import VideoCourseRDTOWithRelated
from app.adapters.filters.video_course.video_course_filter import VideoCourseFilter
from app.adapters.repositories.video_course.video_course_repository import VideoCourseRepository
from app.use_cases.base_case import BaseUseCase


class AllVideoCoursesCase(BaseUseCase[PaginationVideoCourses]):
    def __init__(self, db: AsyncSession):
        self.repository = VideoCourseRepository(db)

    async def execute(self, params: VideoCourseFilter):
        video_courses = await self.repository.paginate(
            dto=VideoCourseRDTOWithRelated,
            page=params.page,
            per_page=params.per_page,
            options=[
                joinedload(self.repository.model.course),
                joinedload(self.repository.model.lang)
            ]
        )
        return video_courses

    async def validate(self):
        pass
