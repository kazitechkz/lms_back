from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.course.course_dto import CourseRDTO
from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.dto.tag.tag_dto import TagRDTO
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetCourseCase(BaseUseCase[CourseRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = CourseRepository(db)

    async def execute(self, course_id: int) -> CourseRDTO:
        course = await self.validate(course_id=course_id)
        return CourseRDTO.from_orm(course)

    async def validate(self, course_id: int):
        course = await self.repository.get(course_id, options=[
            joinedload(self.repository.model.category),
            joinedload(self.repository.model.type)
        ])
        if not course:
            raise AppExceptionResponse.not_found("Курс не найден")
        return course
