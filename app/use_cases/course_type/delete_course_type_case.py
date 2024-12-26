from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.infrastructure.db_constants import AppDbValueConstants
from app.use_cases.base_case import BaseUseCase


class DeleteCourseTypeCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseTypeRepository(db)

    async def execute(self, id: int) -> bool:
        await self.validate(id=id)
        data = await self.repository.delete(id=id)
        return data

    async def validate(self, id: int):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Тип курса не найден")
        if existed.value in AppDbValueConstants.IMMUTABLE_COURSE_TYPES:
            raise AppExceptionResponse.bad_request(message="Тип курса нельзя удалять")
