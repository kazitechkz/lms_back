from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.course_material.course_material_dto import CourseMaterialRDTO, CourseMaterialCDTO, \
    CourseMaterialRDTOWithRelated
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.course_material.course_material_repository import CourseMaterialRepository
from app.adapters.repositories.material.material_repository import MaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateCourseMaterialCase(BaseUseCase[CourseMaterialRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseMaterialRepository(db)
        self.course_repository = CourseRepository(db)
        self.material_repository = MaterialRepository(db)

    async def execute(self, dto: CourseMaterialCDTO) -> CourseMaterialRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj, options=[
            joinedload(self.repository.model.course),
            joinedload(self.repository.model.material)
        ])
        return CourseMaterialRDTO.from_orm(data)

    async def validate(self, dto: CourseMaterialCDTO):
        if await self.course_repository.get(id=dto.course_id) is None:
            raise AppExceptionResponse.bad_request("Курс не найден")
        if await self.material_repository.get(id=dto.material_id) is None:
            raise AppExceptionResponse.bad_request("Материал не найден")
        return self.repository.model(**dto.dict())
