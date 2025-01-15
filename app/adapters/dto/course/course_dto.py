from typing import Optional

from pydantic import BaseModel, Field

from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO
from app.adapters.dto.course_tag.course_tag_dto import CourseTagRDTOWithRelated
from app.adapters.dto.course_type.course_type_dto import CourseTypeRDTO
from app.adapters.dto.language.language_dto import LanguageRDTO
from app.adapters.dto.material.material_dto import MaterialRDTOWithRelated
from app.infrastructure.db_constants import DTOConstant


class CourseDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class CourseRDTO(CourseDTO):
    id: DTOConstant.StandardID
    title: DTOConstant.StandardTitleRu
    short_description: Optional[DTOConstant.StandardText]
    description: DTOConstant.StandardText
    learned: DTOConstant.StandardText
    price: int = Field(default=None, description="Стоимость курса")
    thumbnail: str | None = Field(default=None, description="Обложка курса")
    author: str | None = Field(default=None, description="Автор курса")
    type_id: int = Field(default=None, description="Уникальный ID типа курса")
    category_id: int = Field(default=None, description="Уникальный ID категории курса")
    lang_id: int = Field(default=None, description="Уникальный ID языка")
    tags: Optional[list[int]] = Field(default=None, description="Теги курса")
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class CourseCDTO(BaseModel):
    title: DTOConstant.StandardTitleRu
    short_description: Optional[DTOConstant.StandardText]
    description: DTOConstant.StandardText
    learned: DTOConstant.StandardText
    price: int = Field(default=None, description="Стоимость курса")
    thumbnail: str | None = Field(default=None, description="Обложка курса")
    author: Optional[DTOConstant.StandardValue]
    type_id: int = Field(default=None, description="Уникальный ID типа курса")
    category_id: int = Field(default=None, description="Уникальный ID категории курса")
    lang_id: int = Field(default=None, description="Уникальный ID языка курса")
    tags: Optional[list[int]] = Field(default=None, description="Теги курса")

    class Config:
        from_attributes = True


class CourseRDTOWithRelated(CourseRDTO):
    type: Optional[CourseTypeRDTO] = Field(default=None, description="Тип курса")
    category: Optional[CourseCategoryRDTO] = Field(default=None, description="Категория курса")
    lang: Optional[LanguageRDTO] = Field(default=None, description="Язык курса")
    tags: Optional[list[CourseTagRDTOWithRelated]] = Field(description="Теги курса")
    materials: Optional[list[MaterialRDTOWithRelated]] = Field(description="Материалы курса")

    class Config:
        from_attributes = True
