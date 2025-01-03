from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.video_material.video_material_dto import VideoMaterialRDTOWithRelated
from app.adapters.repositories.video_material.video_material_repository import VideoMaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetVideoMaterialCase(BaseUseCase[VideoMaterialRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = VideoMaterialRepository(db)

    async def execute(self, video_material_id: int) -> VideoMaterialRDTOWithRelated:
        video_material = await self.validate(video_material_id=video_material_id)
        return VideoMaterialRDTOWithRelated.from_orm(video_material)

    async def validate(self, video_material_id: int):
        video_material = await self.repository.get(video_material_id)
        if not video_material:
            raise AppExceptionResponse.not_found("Материал видео не найден")
        return video_material
