from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.blog_category.blog_category_dto import BlogCategoryCDTO, BlogCategoryRDTO
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.blog_category.all_blog_categories_case import AllBlogCategoriesCase
from app.use_cases.blog_category.create_blog_category_case import CreateBlogCategoryCase
from app.use_cases.blog_category.delete_blog_category_case import DeleteBlogCategoryCase
from app.use_cases.blog_category.get_blog_category_by_value_case import GetBlogCategoryByValueCase
from app.use_cases.blog_category.get_blog_category_case import GetBlogCategoryCase
from app.use_cases.blog_category.update_blog_category_case import UpdateBlogCategoryCase


class BlogCategoryApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[BlogCategoryRDTO],
            summary="Список категорий блога",
            description="Получение списка категорий блога",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=BlogCategoryRDTO,
            summary="Получить категорию по уникальному ID",
            description="Получение категории по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=BlogCategoryRDTO,
            summary="Получить категорию по уникальному значению",
            description="Получение категории по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=BlogCategoryRDTO,
            summary="Создать категорию",
            description="Создание категории",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=BlogCategoryRDTO,
            summary="Обновить категорию по уникальному ID",
            description="Обновление категории по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить категорию по уникальному ID",
            description="Удаление категории по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_BLOG_CATEGORY_VALUE))):
        use_case = AllBlogCategoriesCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_BLOG_CATEGORY_VALUE))):
        use_case = GetBlogCategoryCase(db)
        return await use_case.execute(blog_category_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.READ_BLOG_CATEGORY_VALUE))
    ):
        use_case = GetBlogCategoryByValueCase(db)
        return await use_case.execute(blog_category_value=value)

    async def create(self, dto: BlogCategoryCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_BLOG_CATEGORY_VALUE))):
        use_case = CreateBlogCategoryCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: BlogCategoryCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_BLOG_CATEGORY_VALUE))
    ):
        use_case = UpdateBlogCategoryCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_BLOG_CATEGORY_VALUE))
    ):
        use_case = DeleteBlogCategoryCase(db)
        return await use_case.execute(id=id)
