from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.course.course_dto import CourseRDTOWithRelated
from app.adapters.repositories.course.course_repository import CourseRepository
from app.core.app_exception_response import AppExceptionResponse
from app.entities.course_tag import CourseTagModel
from app.use_cases.base_case import BaseUseCase


class GetCourseCase(BaseUseCase[CourseRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = CourseRepository(db)

    async def execute(self, course_id: int) -> CourseRDTOWithRelated:
        course = await self.validate(course_id=course_id)
        return CourseRDTOWithRelated.from_orm(course)

    async def validate(self, course_id: int):
        course = await self.repository.get(course_id, options=[
            selectinload(self.repository.model.category),
            selectinload(self.repository.model.type),
            selectinload(self.repository.model.lang),
            selectinload(self.repository.model.tags).selectinload(CourseTagModel.tag),
            selectinload(self.repository.model.materials)
        ])
        if not course:
            raise AppExceptionResponse.not_found("Курс не найден")
        return course
