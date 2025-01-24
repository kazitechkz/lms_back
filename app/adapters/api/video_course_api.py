from typing import Union

from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.pagination_dto import PaginationVideoCourses
from app.adapters.dto.video_course.video_course_dto import VideoCourseRDTOWithRelated, VideoCourseCDTO
from app.adapters.filters.video_course.video_course_filter import VideoCourseFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.video_course.all_video_courses_case import AllVideoCoursesCase
from app.use_cases.video_course.create_video_course_case import CreateVideoCourseCase
from app.use_cases.video_course.delete_video_course_case import DeleteVideoCourseCase
from app.use_cases.video_course.get_video_course_case import GetVideoCourseCase
from app.use_cases.video_course.update_video_course_case import UpdateVideoCourseCase

def parse_dto_from_form(title: str = Form(...),
                        description: str = Form(...),
                        level: int = Form(...),
                        course_id: int = Form(...),
                        lang_id: int = Form(...),
                        is_first: bool = Form(...),
                        is_last: bool = Form(...)
                        ) -> VideoCourseCDTO:
    return VideoCourseCDTO(
        title=title,
        description=description,
        level=level,
        course_id=course_id,
        lang_id=lang_id,
        is_first=is_first,
        is_last=is_last,
    )
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
            response_model=VideoCourseRDTOWithRelated,
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
                  user=Depends(permission_dependency(PermissionConstants.READ_VIDEO_COURSE_VALUE))):
        use_case = GetVideoCourseCase(db)
        return await use_case.execute(video_course_id=id)

    async def create(self, dto: VideoCourseCDTO = Depends(parse_dto_from_form), db: AsyncSession = Depends(get_db),
                     image: UploadFile = File(default=None, description="Обложка видео"),
                     video: UploadFile = File(default=None, description="Видео"),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_VIDEO_COURSE_VALUE))):
        use_case = CreateVideoCourseCase(db)
        return await use_case.execute(dto=dto, file=image, user=user, video=video)

    async def update(
            self,
            id: PathConstants.IDPath,
            dto: VideoCourseCDTO = Depends(parse_dto_from_form),
            image: Union[UploadFile, str, None] = File(default=None, description="Обложка видео"),
            video: UploadFile | None = File(default=None, description="Видео"),
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_VIDEO_COURSE_VALUE))
    ):
        use_case = UpdateVideoCourseCase(db)
        return await use_case.execute(id=id, dto=dto, image=image, video=video, user=user)

    async def delete(
            self,
            id: PathConstants.IDPath,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_VIDEO_COURSE_VALUE))
    ):
        use_case = DeleteVideoCourseCase(db)
        return await use_case.execute(id=id)
