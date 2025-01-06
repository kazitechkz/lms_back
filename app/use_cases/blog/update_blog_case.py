from typing import Optional

from fastapi import File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.blog.blog_dto import BlogRDTOWithRelated, BlogCDTO
from app.adapters.repositories.blog.blog_repository import BlogRepository
from app.adapters.repositories.blog_category.blog_category_repository import BlogCategoryRepository
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.delete_file_case import DeleteFileCase
from app.use_cases.file.upload_file_case import UploadFileCase


class UpdateBlogCase(BaseUseCase[BlogRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = BlogRepository(db)
        self.category_repo = BlogCategoryRepository(db)
        self.lang_repo = LanguageRepository(db)
        self.upload_file_use_case = UploadFileCase(db)
        self.delete_file_use_case = DeleteFileCase(db)

    async def execute(self, id: int, dto: BlogCDTO, file: Optional[File] = None) -> BlogRDTOWithRelated:
        blog = await self.validate(id=id, dto=dto, file=file)
        data = await self.repository.update(obj=blog, dto=dto, options=[
            selectinload(self.repository.model.category),
            selectinload(self.repository.model.lang)
        ])
        return BlogRDTOWithRelated.from_orm(data)

    async def validate(self, id: int, dto: BlogCDTO, file: Optional[File] = None):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Блог не найден")
        if dto.category_id:
            if not await self.category_repo.get(id=dto.category_id):
                raise AppExceptionResponse.not_found(message="Категория курса не найдена")
        if not await self.lang_repo.get(id=dto.lang_id):
            raise AppExceptionResponse.not_found(message="Язык не найден")
        if file:
            file_data = await self.upload_file_use_case.execute(file=file, upload_path="blog_thumbnails/")
            dto.thumbnail = file_data
            await self.delete_file_use_case.execute(url=existed.thumbnail)
        else:
            dto.thumbnail = existed.thumbnail
        return existed
