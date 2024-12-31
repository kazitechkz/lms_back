from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.course.course_repository import CourseRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.course_tag.delete_course_tag_case import DeleteCourseTagCase
from app.use_cases.file.delete_file_case import DeleteFileCase


class DeleteCourseCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseRepository(db)
        self.delete_course_tag_use_case = DeleteCourseTagCase(db)
        self.delete_file_use_case = DeleteFileCase(db)

    async def execute(self, id: int) -> bool:
        await self.validate(id=id)
        await self.delete_course_tag_use_case.execute(id)
        data = await self.repository.delete(id=id)
        return data

    async def validate(self, id: int):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Курс не найден")
        if existed.thumbnail is not None:
            await self.delete_file_use_case.execute(existed.thumbnail)
