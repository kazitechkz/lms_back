from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.blog_category.blog_category_dto import BlogCategoryRDTO, BlogCategoryCDTO
from app.adapters.repositories.blog_category.blog_category_repository import BlogCategoryRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateBlogCategoryCase(BaseUseCase[BlogCategoryRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = BlogCategoryRepository(db)

    async def execute(self, id: int, dto: BlogCategoryCDTO) -> BlogCategoryRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return BlogCategoryRDTO.from_orm(data)

    async def validate(self, id: int, dto: BlogCategoryCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Категория блога не найдена")
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value, self.repository.model.id != id]
        ):
            raise AppExceptionResponse.bad_request(
                "Категория блога с таким значением уже существует"
            )
        return existed
