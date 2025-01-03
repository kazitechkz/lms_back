from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.video_material.video_material_dto import VideoMaterialRDTO, VideoMaterialCDTO, \
    VideoMaterialRDTOWithRelated
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.video_material.create_video_material_case import CreateVideoMaterialCase
from app.use_cases.video_material.delete_course_material_case import DeleteVideoMaterialCase
from app.use_cases.video_material.get_video_material_case import GetVideoMaterialCase
from app.use_cases.video_material.update_video_material_case import UpdateVideoMaterialCase


class VideoMaterialApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.post(
            "/get/{id}",
            response_model=VideoMaterialRDTOWithRelated,
            summary="Получить материал видео по ID",
            description="Получение материала видео по ID",
        )(self.get)
        self.router.post(
            "/create",
            response_model=VideoMaterialRDTO,
            summary="Создать материал видео",
            description="Создание материала видео",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=VideoMaterialRDTO,
            summary="Обновить материал видео",
            description="Обновление материала видео",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить материал видео по уникальному ID",
            description="Удаление материала видео по уникальному идентификатору",
        )(self.delete)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_VIDEO_MATERIAL_VALUE))):
        use_case = GetVideoMaterialCase(db)
        return await use_case.execute(video_material_id=id)

    async def create(self, dto: VideoMaterialCDTO,
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_VIDEO_MATERIAL_VALUE))):
        use_case = CreateVideoMaterialCase(db)
        return await use_case.execute(dto=dto)

    async def update(self, id: PathConstants.IDPath, dto: VideoMaterialCDTO,
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.UPDATE_VIDEO_MATERIAL_VALUE))):
        use_case = UpdateVideoMaterialCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
            self,
            id: PathConstants.IDPath,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_VIDEO_MATERIAL_VALUE))
    ):
        use_case = DeleteVideoMaterialCase(db)
        return await use_case.execute(id=id)
