from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_material.course_material_dto import CourseMaterialRDTO, CourseMaterialCDTO
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.course_material.course_material_repository import CourseMaterialRepository
from app.adapters.repositories.material.material_repository import MaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateCourseMaterialCase(BaseUseCase[CourseMaterialRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseMaterialRepository(db)
        self.course_repository = CourseRepository(db)
        self.material_repository = MaterialRepository(db)

    async def execute(self, id: int, dto: CourseMaterialCDTO) -> CourseMaterialRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return CourseMaterialRDTO.from_orm(data)

    async def validate(self, id: int, dto: CourseMaterialCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Материал курса не найден")
        if await self.course_repository.get(id=dto.course_id) is None:
            raise AppExceptionResponse.not_found(message="Курс не найден")
        if await self.material_repository.get(id=dto.material_id) is None:
            raise AppExceptionResponse.not_found(message="Материал не найден")
        return existed
