from pydantic import BaseModel

from app.adapters.dto.tag.tag_dto import TagRDTO
from app.infrastructure.db_constants import DTOConstant


class CourseTagDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class CourseTagRDTO(CourseTagDTO):
    id: DTOConstant.StandardID
    course_id: DTOConstant.StandardID
    tag_id: DTOConstant.StandardID

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class CourseTagCDTO(BaseModel):
    course_id: DTOConstant.StandardID
    tag_id: DTOConstant.StandardID


class CourseTagRDTOWithRelated(CourseTagRDTO):
    tag: TagRDTO
