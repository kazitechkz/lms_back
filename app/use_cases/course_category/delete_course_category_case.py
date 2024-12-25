from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class DeleteCourseCategoryCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.course_category_repository = CourseCategoryRepository(db)

    async def execute(self, id: int, delete_cascade: bool = False) -> bool:
        data = await self.validate(repository=self.course_category_repository, id=id)
        if data.children is not None and delete_cascade:
            for child in data.children:
                await self.course_category_repository.delete(id=child.id)
        data = await self.course_category_repository.delete(id=id)
        return data

    async def validate(self, repository: CourseCategoryRepository, id: int):
        existed = await self.course_category_repository.get(id=id, options=[selectinload(repository.model.children)])
        if existed is None:
            raise AppExceptionResponse.not_found(message="Категория не найдена")
        return existed
