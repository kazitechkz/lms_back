from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.blog_category.blog_category_dto import BlogCategoryRDTO
from app.adapters.repositories.blog_category.blog_category_repository import BlogCategoryRepository
from app.use_cases.base_case import BaseUseCase


class AllBlogCategoriesCase(BaseUseCase[List[BlogCategoryRDTO]]):
    def __init__(self, db: AsyncSession):
        self.repository = BlogCategoryRepository(db)

    async def execute(self) -> List[BlogCategoryRDTO]:
        blog_categories = await self.repository.get_all()
        return [BlogCategoryRDTO.from_orm(blog_category) for blog_category in blog_categories]

    async def validate(self):
        pass
