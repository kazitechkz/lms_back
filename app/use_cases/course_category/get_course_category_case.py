from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO
from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetCourseCategoryCase(BaseUseCase[CourseCategoryRDTO]):
    """Use Case для получения роли по ID."""

    def __init__(self, db: AsyncSession):
        self.course_category_repository = CourseCategoryRepository(db)

    async def execute(self, course_category_id: int) -> RoleRDTO:
        obj = await self.validate(repository=self.course_category_repository, course_category_id=course_category_id)
        return CourseCategoryRDTO.from_orm(obj)

    async def validate(self, repository: CourseCategoryRepository, course_category_id: int):
        course_category = await self.course_category_repository.get(course_category_id,
                                                                    options=[selectinload(repository.model.parent)])
        if not course_category:
            raise AppExceptionResponse.not_found("Категория не найдена")
        return course_category
