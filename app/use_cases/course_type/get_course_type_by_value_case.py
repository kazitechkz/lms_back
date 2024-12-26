from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_type.course_type_dto import CourseTypeRDTO
from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetCourseTypeByValueCase(BaseUseCase[CourseTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.role_repository = CourseTypeRepository(db)

    async def execute(self, role_value: str) -> CourseTypeRDTO:
        role = await self.validate(role_value=role_value)
        return CourseTypeRDTO.from_orm(role)

    async def validate(self, role_value: str):
        filters = [self.role_repository.model.value == role_value]
        role = await self.role_repository.get_first_with_filters(filters)
        if not role:
            raise AppExceptionResponse.not_found("Тип курса не найден")
        return role
