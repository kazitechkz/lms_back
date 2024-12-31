from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.pagination_dto import PaginationVideoCourses
from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.dto.video_course.video_course_dto import VideoCourseRDTOWithRelated, VideoCourseCDTO, VideoCourseRDTO
from app.adapters.filters.video_course.video_course_filter import VideoCourseFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase
from app.use_cases.video_course.all_video_courses_case import AllVideoCoursesCase
from app.use_cases.video_course.create_video_course_case import CreateVideoCourseCase
from app.use_cases.video_course.delete_video_course_case import DeleteVideoCourseCase
from app.use_cases.video_course.update_video_course_case import UpdateVideoCourseCase


class VideoCourseApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=PaginationVideoCourses,
            summary="Список видеокурсов",
            description="Получение списка видеокурсов",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=VideoCourseRDTOWithRelated,
            summary="Получить видеокурс по уникальному ID",
            description="Получение видеокурса по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=VideoCourseRDTOWithRelated,
            summary="Создать видеокурса",
            description="Создание видеокурса",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=VideoCourseRDTO,
            summary="Обновить видеокурс по уникальному ID",
            description="Обновление видеокурса по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить видеокурс по уникальному ID",
            description="Удаление видеокурса по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      params: VideoCourseFilter = Depends(),
                      user=Depends(permission_dependency(PermissionConstants.READ_VIDEO_COURSE_VALUE))):
        use_case = AllVideoCoursesCase(db)
        return await use_case.execute(params=params)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))):
        use_case = GetTagCase(db)
        return await use_case.execute(tag_id=id)

    async def create(self, dto: VideoCourseCDTO = Depends(), db: AsyncSession = Depends(get_db),
                     image: UploadFile = File(default=None, description="Обложка видео"),
                     video: UploadFile = File(default=None, description="Видео"),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_VIDEO_COURSE_VALUE))):
        use_case = CreateVideoCourseCase(db)
        return await use_case.execute(dto=dto, file=image, user=user, video=video)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: VideoCourseCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_VIDEO_COURSE_VALUE))
    ):
        use_case = UpdateVideoCourseCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_VIDEO_COURSE_VALUE))
    ):
        use_case = DeleteVideoCourseCase(db)
        return await use_case.execute(id=id)
