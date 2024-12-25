from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetCourseCategoryByValueCase(BaseUseCase[CourseCategoryRDTO]):
    def __init__(self, db: AsyncSession):
        self.course_category_repository = CourseCategoryRepository(db)

    async def execute(self, course_category_value: str) -> CourseCategoryRDTO:
        obj = await self.validate(self.course_category_repository, value=course_category_value)
        return CourseCategoryRDTO.from_orm(obj)

    async def validate(self, repo: CourseCategoryRepository, value: str):
        filters = [self.course_category_repository.model.value == value]
        course_category = await self.course_category_repository.get_first_with_filters(
            filters=filters, options=[selectinload(repo.model.parent)])
        if not course_category:
            raise AppExceptionResponse.not_found("Категория не найдена")
        return course_category
