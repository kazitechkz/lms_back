from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.video_material.video_material_dto import VideoMaterialRDTO, VideoMaterialCDTO
from app.adapters.repositories.material.material_repository import MaterialRepository
from app.adapters.repositories.video_course.video_course_repository import VideoCourseRepository
from app.adapters.repositories.video_material.video_material_repository import VideoMaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateVideoMaterialCase(BaseUseCase[VideoMaterialRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = VideoMaterialRepository(db)
        self.video_repository = VideoCourseRepository(db)
        self.material_repository = MaterialRepository(db)

    async def execute(self, dto: VideoMaterialCDTO) -> VideoMaterialRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj, options=[
            joinedload(self.repository.model.video),
            joinedload(self.repository.model.material)
        ])
        return VideoMaterialRDTO.from_orm(data)

    async def validate(self, dto: VideoMaterialCDTO):
        if await self.video_repository.get(id=dto.video_id) is None:
            raise AppExceptionResponse.bad_request("Видеокурс не найден")
        if await self.material_repository.get(id=dto.material_id) is None:
            raise AppExceptionResponse.bad_request("Материал не найден")
        return self.repository.model(**dto.dict())
