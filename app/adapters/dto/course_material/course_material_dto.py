from pydantic import BaseModel, Field

from app.adapters.dto.course.course_dto import CourseRDTO
from app.adapters.dto.material.material_dto import MaterialRDTOWithRelated
from app.infrastructure.db_constants import DTOConstant


class CourseMaterialDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class CourseMaterialRDTO(CourseMaterialDTO):
    id: DTOConstant.StandardID
    course_id: int = Field(description="Уникальный ID курса")
    material_id: int = Field(description="Уникальный ID материала")
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class CourseMaterialCDTO(BaseModel):
    course_id: int = Field(description="Уникальный ID курса")
    material_id: int = Field(description="Уникальный ID материала")

    class Config:
        from_attributes = True


class CourseMaterialRDTOWithRelated(CourseMaterialRDTO):
    course: CourseRDTO
    material: MaterialRDTOWithRelated
