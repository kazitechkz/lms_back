from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO, CourseCategoryCDTO
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateCourseCategoryCase(BaseUseCase[CourseCategoryRDTO]):
    def __init__(self, db: AsyncSession):
        self.course_category_repository = CourseCategoryRepository(db)

    async def execute(self, id: int, dto: CourseCategoryCDTO) -> CourseCategoryRDTO:
        obj = await self.validate(repository=self.course_category_repository, cat_id=id, dto=dto)
        data = await self.course_category_repository.update(
            obj=obj, dto=dto,
            options=[
                selectinload(self.course_category_repository.model.parent),
                selectinload(self.course_category_repository.model.children)
            ]
        )
        return CourseCategoryRDTO.from_orm_with_depth(data, depth=1)

    async def validate(self, repository: CourseCategoryRepository, cat_id: int, dto: CourseCategoryCDTO):
        existed = await repository.get(id=cat_id, options=[selectinload(repository.model.children)])
        if existed is None:
            raise AppExceptionResponse.not_found(message="Категория курса не найдена")
        if await repository.get_first_with_filters(
            [repository.model.value == dto.value, repository.model.id != cat_id]
        ):
            raise AppExceptionResponse.bad_request(
                "Категория с таким значением уже существует"
            )
        if dto.parent_id is not None:
            if existed.children is not None:
                raise AppExceptionResponse.bad_request(
                    "Категория содержит дочерние категории и не может быть присвоена другой категории"
                )
            parent = await repository.get(id=dto.parent_id)
            if not parent:
                raise AppExceptionResponse.bad_request("Родительская категория не найдена")
            if parent.parent_id is not None:
                raise AppExceptionResponse.bad_request(
                    "Родительская категория не может быть вложенной в другую вложенную категорию"
                )
        return existed
