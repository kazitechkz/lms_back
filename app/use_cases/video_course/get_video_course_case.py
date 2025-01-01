from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.video_course.video_course_dto import VideoCourseRDTOWithRelated
from app.adapters.repositories.video_course.video_course_repository import VideoCourseRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetVideoCourseCase(BaseUseCase[VideoCourseRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = VideoCourseRepository(db)

    async def execute(self, video_course_id: int) -> VideoCourseRDTOWithRelated:
        video_course = await self.validate(video_course_id=video_course_id)
        return VideoCourseRDTOWithRelated.from_orm(video_course)

    async def validate(self, video_course_id: int):
        video_course = await self.repository.get(id=video_course_id, options=[
            joinedload(self.repository.model.lang)
        ])
        if not video_course:
            raise AppExceptionResponse.not_found("Видеокурс не найден")
        return video_course
