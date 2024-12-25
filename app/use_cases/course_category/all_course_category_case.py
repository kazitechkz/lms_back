from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.use_cases.base_case import BaseUseCase


class AllCourseCategoryCase(BaseUseCase[List[CourseCategoryRDTO]]):
    def __init__(self, db: AsyncSession):
        self.course_category_repository = CourseCategoryRepository(db)

    async def execute(self) -> List[CourseCategoryRDTO]:
        course_categories = await self.course_category_repository.get_all(
            options=[
                selectinload(self.course_category_repository.model.parent),
                selectinload(self.course_category_repository.model.children)
            ]
        )
        return [
            CourseCategoryRDTO.from_orm_with_depth(course_category, depth=1)
            for course_category in course_categories
        ]

    async def validate(self):
        pass
