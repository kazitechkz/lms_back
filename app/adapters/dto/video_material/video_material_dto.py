from pydantic import BaseModel, Field

from app.adapters.dto.material.material_dto import MaterialRDTOWithRelated
from app.adapters.dto.video_course.video_course_dto import VideoCourseRDTO
from app.infrastructure.db_constants import DTOConstant


class VideoMaterialDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class VideoMaterialRDTO(VideoMaterialDTO):
    id: DTOConstant.StandardID
    video_id: int | None = Field(default=None, description="Уникальный ID видеокурса")
    material_id: int | None = Field(default=None, description="Уникальный ID материала")
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class VideoMaterialCDTO(BaseModel):
    video_id: int | None = Field(default=None, description="Уникальный ID видеокурса")
    material_id: int | None = Field(default=None, description="Уникальный ID материала")

    class Config:
        from_attributes = True


class VideoMaterialRDTOWithRelated(VideoMaterialRDTO):
    video: VideoCourseRDTO
    material: MaterialRDTOWithRelated
