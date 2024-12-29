from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, selectinload

from app.adapters.dto.course.course_dto import CourseRDTO, CourseCDTO, CourseRDTOWithRelated
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.core.app_exception_response import AppExceptionResponse
from app.entities.course_tag import CourseTagModel
from app.use_cases.base_case import BaseUseCase
from app.use_cases.course_tag.create_course_tag_case import CreateCourseTagCase
from app.use_cases.course_tag.update_course_tag_case import UpdateCourseTagCase


class UpdateCourseCase(BaseUseCase[CourseRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseRepository(db)
        self.type_repo = CourseTypeRepository(db)
        self.category_repo = CourseCategoryRepository(db)
        self.lang_repo = LanguageRepository(db)
        self.course_create_tag_use_case = CreateCourseTagCase(db)
        self.course_update_tag_use_case = UpdateCourseTagCase(db)

    async def execute(self, id: int, dto: CourseCDTO) -> CourseRDTOWithRelated:
        course = await self.validate(id=id)
        updated_dto = await self.exclude_tags(dto=dto)
        tag_data = await self.course_update_tag_use_case.validate(tag_ids=dto.tags, course_id=id)
        data = await self.repository.update(obj=course, dto=updated_dto, options=[
            selectinload(self.repository.model.category),
            selectinload(self.repository.model.type),
            selectinload(self.repository.model.lang),
            selectinload(self.repository.model.tags).selectinload(CourseTagModel.tag),
        ])
        if tag_data:
            await self.course_create_tag_use_case.execute(tag_ids=tag_data, course_id=course.id)
        return CourseRDTOWithRelated.from_orm(data)

    async def validate(self, id: int):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Курс не найден")
        return existed

    async def exclude_tags(self, dto: CourseCDTO):
        if not await self.type_repo.get(id=dto.type_id):
            raise AppExceptionResponse.not_found(message="Тип курса не найден")
        if not await self.category_repo.get(id=dto.category_id):
            raise AppExceptionResponse.not_found(message="Категория курса не найдена")
        if not await self.lang_repo.get(id=dto.lang_id):
            raise AppExceptionResponse.not_found(message="Язык не найден")
        data = dto.dict(exclude={"tags"})  # Удаляем tags из словаря
        return CourseCDTO.from_orm(data)
