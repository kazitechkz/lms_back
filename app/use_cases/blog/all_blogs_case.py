from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.blog.blog_dto import BlogRDTOWithRelated
from app.adapters.dto.pagination_dto import PaginationBlogs
from app.adapters.filters.blog.blog_filter import BlogFilter
from app.adapters.repositories.blog.blog_repository import BlogRepository
from app.use_cases.base_case import BaseUseCase


class AllBlogsCase(BaseUseCase[PaginationBlogs]):
    def __init__(self, db: AsyncSession, params: BlogFilter):
        self.repository = BlogRepository(db)
        self.params = params

    async def execute(self):
        blogs = await self.repository.paginate(
            dto=BlogRDTOWithRelated,
            page=self.params.page,
            per_page=self.params.per_page,
            filters=self.params.apply(),
            options=[
                selectinload(self.repository.model.category),
                selectinload(self.repository.model.lang)
            ]
        )

        return blogs

    async def validate(self):
        pass
