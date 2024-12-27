from sqlalchemy import Boolean
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.course.course_dto import CourseRDTO, CourseCDTO
from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.core.app_exception_response import AppExceptionResponse
from app.entities import CourseCategoryModel
from app.use_cases.base_case import BaseUseCase


class CreateCourseCase(BaseUseCase[CourseRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseRepository(db)
        self.type_repo = CourseTypeRepository(db)
        self.category_repo = CourseCategoryRepository(db)

    async def execute(self, dto: CourseCDTO) -> bool:
        obj = await self.validate(dto=dto)
        await self.repository.create(obj=obj)
        return True

    async def validate(self, dto: CourseCDTO):
        if not await self.type_repo.get(id=dto.type_id):
            raise AppExceptionResponse.not_found(message="Тип курса не найден")
        if not await self.category_repo.get(id=dto.category_id):
            raise AppExceptionResponse.not_found(message="Категория курса не найдена")
        return self.repository.model(**dto.dict())
