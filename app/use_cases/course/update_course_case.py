from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.course.course_dto import CourseRDTO, CourseCDTO
from app.adapters.dto.tag.tag_dto import TagCDTO, TagRDTO
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateCourseCase(BaseUseCase[CourseRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseRepository(db)
        self.type_repo = CourseTypeRepository(db)
        self.category_repo = CourseCategoryRepository(db)

    async def execute(self, id: int, dto: CourseCDTO) -> CourseRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto, options=[
            joinedload(self.repository.model.category),
            joinedload(self.repository.model.type)
        ])
        return CourseRDTO.from_orm(data)

    async def validate(self, id: int, dto: CourseCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Курс не найден")
        if not await self.type_repo.get(id=dto.type_id):
            raise AppExceptionResponse.not_found(message="Тип курса не найден")
        if not await self.category_repo.get(id=dto.category_id):
            raise AppExceptionResponse.not_found(message="Категория курса не найдена")
        return existed
