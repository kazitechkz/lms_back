from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.video_material.video_material_dto import VideoMaterialCDTO, VideoMaterialRDTO
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.material.material_repository import MaterialRepository
from app.adapters.repositories.video_course.video_course_repository import VideoCourseRepository
from app.adapters.repositories.video_material.video_material_repository import VideoMaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateVideoMaterialCase(BaseUseCase[VideoMaterialRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = VideoMaterialRepository(db)
        self.video_repository = VideoCourseRepository(db)
        self.material_repository = MaterialRepository(db)

    async def execute(self, id: int, dto: VideoMaterialCDTO) -> VideoMaterialRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return VideoMaterialRDTO.from_orm(data)

    async def validate(self, id: int, dto: VideoMaterialCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Материал курса не найден")
        if await self.video_repository.get(id=dto.video_id) is None:
            raise AppExceptionResponse.not_found(message="Видеокурс не найден")
        if await self.material_repository.get(id=dto.material_id) is None:
            raise AppExceptionResponse.not_found(message="Материал не найден")
        return existed
