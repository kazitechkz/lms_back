from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.blog_category.blog_category_dto import BlogCategoryRDTO
from app.adapters.repositories.blog_category.blog_category_repository import BlogCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetBlogCategoryCase(BaseUseCase[BlogCategoryRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = BlogCategoryRepository(db)

    async def execute(self, blog_category_id: int) -> BlogCategoryRDTO:
        blog_category = await self.validate(blog_category_id=blog_category_id)
        return BlogCategoryRDTO.from_orm(blog_category)

    async def validate(self, blog_category_id: int):
        blog_category = await self.repository.get(blog_category_id)
        if not blog_category:
            raise AppExceptionResponse.not_found("Категория блога не найдена")
        return blog_category
