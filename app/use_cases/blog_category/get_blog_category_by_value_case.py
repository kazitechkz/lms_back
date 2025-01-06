from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.blog_category.blog_category_dto import BlogCategoryRDTO
from app.adapters.repositories.blog_category.blog_category_repository import BlogCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetBlogCategoryByValueCase(BaseUseCase[BlogCategoryRDTO]):
    def __init__(self, db: AsyncSession):
        self.tag_repository = BlogCategoryRepository(db)

    async def execute(self, blog_category_value: str) -> BlogCategoryRDTO:
        blog_category = await self.validate(blog_category_value=blog_category_value)
        return BlogCategoryRDTO.from_orm(blog_category)

    async def validate(self, blog_category_value: str):
        filters = [self.tag_repository.model.value == blog_category_value]
        blog_category = await self.tag_repository.get_first_with_filters(filters)
        if not blog_category:
            raise AppExceptionResponse.not_found("Категория блога не найдена")
        return blog_category
