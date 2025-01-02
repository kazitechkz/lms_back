from typing import Optional

from pydantic import BaseModel, Field

from app.adapters.dto.language.language_dto import LanguageRDTO
from app.infrastructure.db_constants import DTOConstant


class VideoCourseDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class VideoCourseRDTO(VideoCourseDTO):
    id: DTOConstant.StandardID
    title: DTOConstant.StandardVarchar
    video_id: DTOConstant.StandardID
    image: DTOConstant.StandardText
    description: DTOConstant.StandardText
    level: DTOConstant.StandardInteger
    is_first: DTOConstant.StandardBoolean
    is_last: DTOConstant.StandardBoolean
    course_id: DTOConstant.StandardID
    lang_id: DTOConstant.StandardID
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class VideoCourseCDTO(BaseModel):
    title: DTOConstant.StandardVarchar
    video_id: int | None = Field(default=None, description="URL видео")
    image: str | None = Field(default=None, description="Видео обложка")
    description: DTOConstant.StandardText
    level: DTOConstant.StandardInteger
    is_first: DTOConstant.StandardBoolean
    is_last: DTOConstant.StandardBoolean
    course_id: DTOConstant.StandardID
    lang_id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class VideoCourseRDTOWithRelated(VideoCourseRDTO):
    lang: LanguageRDTO
