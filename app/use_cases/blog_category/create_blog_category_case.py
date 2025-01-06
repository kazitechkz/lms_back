from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.blog_category.blog_category_dto import BlogCategoryRDTO, BlogCategoryCDTO
from app.adapters.repositories.blog_category.blog_category_repository import BlogCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateBlogCategoryCase(BaseUseCase[BlogCategoryRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = BlogCategoryRepository(db)

    async def execute(self, dto: BlogCategoryCDTO) -> BlogCategoryRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return BlogCategoryRDTO.from_orm(data)

    async def validate(self, dto: BlogCategoryCDTO):
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Категория блога с таким значением уже существует"
            )
        return self.repository.model(**dto.dict())
