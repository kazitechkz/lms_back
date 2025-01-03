from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_material.course_material_dto import CourseMaterialRDTO
from app.adapters.repositories.course_material.course_material_repository import CourseMaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetCourseMaterialCase(BaseUseCase[CourseMaterialRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = CourseMaterialRepository(db)

    async def execute(self, course_material_id: int) -> CourseMaterialRDTO:
        course_material = await self.validate(course_material_id=course_material_id)
        return CourseMaterialRDTO.from_orm(course_material)

    async def validate(self, course_material_id: int):
        course_material = await self.repository.get(course_material_id)
        if not course_material:
            raise AppExceptionResponse.not_found("Материал курса не найден")
        return course_material
