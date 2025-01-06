from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.blog.blog_repository import BlogRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.delete_file_case import DeleteFileCase


class DeleteBlogCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = BlogRepository(db)
        self.delete_file_use_case = DeleteFileCase(db)

    async def execute(self, id: int) -> bool:
        await self.validate(id=id)
        data = await self.repository.delete(id=id)
        return data

    async def validate(self, id: int):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Блог не найден")
        if existed.thumbnail is not None:
            await self.delete_file_use_case.execute(str(existed.thumbnail))
