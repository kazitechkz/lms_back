from typing import Optional

from fastapi import File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from app.adapters.dto.course.course_dto import CourseRDTO, CourseCDTO, CourseRDTOWithRelated
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.course_tag.create_course_tag_case import CreateCourseTagCase
from app.use_cases.file.upload_file_case import UploadFileCase


class CreateCourseCase(BaseUseCase[CourseRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseRepository(db)
        self.type_repo = CourseTypeRepository(db)
        self.category_repo = CourseCategoryRepository(db)
        self.lang_repo = LanguageRepository(db)
        self.course_tag_use_case = CreateCourseTagCase(db)
        self.upload_file_use_case = UploadFileCase(db)

    async def execute(self, dto: CourseCDTO, file: Optional[File] = None) -> CourseRDTOWithRelated:
        course_data = await self.validate(dto=dto, file=file)
        tag_data = await self.course_tag_use_case.validate(tag_ids=dto.tags)
        course = await self.repository.create(obj=course_data, options=[
            joinedload(self.repository.model.type),
            joinedload(self.repository.model.category),
            joinedload(self.repository.model.lang),
            selectinload(self.repository.model.tags),
            selectinload(self.repository.model.materials)
        ])
        if tag_data:
            await self.course_tag_use_case.execute(tag_ids=tag_data, course_id=course.id)
        return CourseRDTOWithRelated.from_orm(course)

    async def validate(self, dto: CourseCDTO, file: Optional[File] = None):
        if not await self.type_repo.get(id=dto.type_id):
            raise AppExceptionResponse.not_found(message="Тип курса не найден")
        if not await self.category_repo.get(id=dto.category_id):
            raise AppExceptionResponse.not_found(message="Категория курса не найдена")
        if not await self.lang_repo.get(id=dto.lang_id):
            raise AppExceptionResponse.not_found(message="Язык не найден")
        if file:
            file_data = await self.upload_file_use_case.execute(file=file, upload_path="course_thumbnails/")
            dto.thumbnail = file_data
        data = dto.dict(exclude={"tags"})  # Удаляем tags из словаря
        return self.repository.model(**data)
