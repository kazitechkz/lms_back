from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.course_category.course_category_dto import CourseCategoryCDTO, \
    CourseCategoryRDTOWithRelated
from app.adapters.repositories.course_category.course_category_repository import CourseCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateCourseCategoryCase(BaseUseCase[CourseCategoryRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.course_category_repository = CourseCategoryRepository(db)

    async def execute(self, dto: CourseCategoryCDTO) -> CourseCategoryRDTOWithRelated:
        obj = await self.validate(repository=self.course_category_repository, dto=dto)
        data = await self.course_category_repository.create(
            obj=obj,
            options=[
                selectinload(self.course_category_repository.model.parent),
                selectinload(self.course_category_repository.model.children)
            ]
        )
        return CourseCategoryRDTOWithRelated.from_orm_with_depth(data, depth=1)

    async def validate(self, repository: CourseCategoryRepository, dto: CourseCategoryCDTO):
        if await repository.get_first_with_filters(
            [repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Категория с таким значением уже существует"
            )
        if dto.parent_id is not None:
            parent = await repository.get(
                id=dto.parent_id,
                options=[
                    selectinload(self.course_category_repository.model.parent),
                    selectinload(self.course_category_repository.model.children)
                ]
            )
            if not parent:
                raise AppExceptionResponse.bad_request("Родительская категория не найдена")
            if parent.parent_id is not None:
                raise AppExceptionResponse.bad_request(
                    "Родительская категория не может быть вложенной в другую вложенную категорию"
                )
        data = dto.dict(exclude_unset=True)  # Исключаем неустановленные поля
        return repository.model(**data)
