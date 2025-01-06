from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.blog.blog_dto import BlogRDTOWithRelated
from app.adapters.repositories.blog.blog_repository import BlogRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetBlogCase(BaseUseCase[BlogRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = BlogRepository(db)

    async def execute(self, blog_id: int) -> BlogRDTOWithRelated:
        blog = await self.validate(blog_id=blog_id)
        return BlogRDTOWithRelated.from_orm(blog)

    async def validate(self, blog_id: int):
        blog = await self.repository.get(blog_id, options=[
            selectinload(self.repository.model.category),
            selectinload(self.repository.model.lang)
        ])
        if not blog:
            raise AppExceptionResponse.not_found("Блог не найден")
        return blog
