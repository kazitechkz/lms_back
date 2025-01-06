from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.blog.blog_dto import BlogCDTO, BlogRDTOWithRelated
from app.adapters.dto.pagination_dto import PaginationBlogs
from app.adapters.filters.blog.blog_filter import BlogFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.blog.all_blogs_case import AllBlogsCase
from app.use_cases.blog.create_blog_case import CreateBlogCase
from app.use_cases.blog.delete_blog_case import DeleteBlogCase
from app.use_cases.blog.get_blog_case import GetBlogCase
from app.use_cases.blog.update_blog_case import UpdateBlogCase


class BlogApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=PaginationBlogs,
            summary="Список новостей",
            description="Получение списка новостей",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=BlogRDTOWithRelated,
            summary="Получить новость по уникальному ID",
            description="Получение новости по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=BlogRDTOWithRelated,
            summary="Создать новость",
            description="Создание новости",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=BlogRDTOWithRelated,
            summary="Обновить новость по уникальному ID",
            description="Обновление новости по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить новость по уникальному ID",
            description="Удаление новости по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db), params: BlogFilter = Depends(),
                      user=Depends(permission_dependency(PermissionConstants.READ_COURSE_VALUE))):
        use_case = AllBlogsCase(db=db, params=params)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_COURSE_VALUE))):
        use_case = GetBlogCase(db)
        return await use_case.execute(blog_id=id)

    async def create(self, dto: BlogCDTO = Depends(),
                     db: AsyncSession = Depends(get_db),
                     thumbnail: UploadFile | None = File(default=None, description="Обложка блога"),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_COURSE_VALUE))):
        use_case = CreateBlogCase(db)
        return await use_case.execute(dto=dto, file=thumbnail)

    async def update(
            self,
            id: PathConstants.IDPath,
            dto: BlogCDTO = Depends(),
            thumbnail: UploadFile | None = File(default=None, description="Обложка блога"),
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_COURSE_VALUE))
    ):
        use_case = UpdateBlogCase(db)
        return await use_case.execute(id=id, dto=dto, file=thumbnail)

    async def delete(
            self,
            id: PathConstants.IDPath,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_COURSE_VALUE))
    ):
        use_case = DeleteBlogCase(db)
        return await use_case.execute(id=id)
