from typing import Optional

from pydantic import BaseModel, Field

from app.adapters.dto.course_category.course_category_dto import CourseCategoryRDTO
from app.adapters.dto.course_type.course_type_dto import CourseTypeRDTO
from app.infrastructure.db_constants import DTOConstant


class CourseDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class CourseRDTO(CourseDTO):
    id: DTOConstant.StandardID
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    short_description_ru: DTOConstant.StandardText
    short_description_kk: DTOConstant.StandardText
    short_description_en: DTOConstant.StandardText
    description_ru: DTOConstant.StandardText
    description_kk: DTOConstant.StandardText
    description_en: DTOConstant.StandardText
    learned_after_course_ru: DTOConstant.StandardText
    learned_after_course_kk: DTOConstant.StandardText
    learned_after_course_en: DTOConstant.StandardText
    price: int = Field(default=None, description="Стоимость курса")
    thumbnail: DTOConstant.StandardValue
    author: DTOConstant.StandardValue
    type_id: int = Field(default=None, description="Уникальный ID типа курса")
    category_id: int = Field(default=None, description="Уникальный ID категории курса")

    type: Optional[CourseTypeRDTO] = Field(default=None, description="Тип курса")
    category: Optional[CourseCategoryRDTO] = Field(default=None, description="Категория курса")

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class CourseCDTO(BaseModel):
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: Optional[DTOConstant.StandardTitleEn]
    short_description_ru: DTOConstant.StandardText
    short_description_kk: DTOConstant.StandardText
    short_description_en: Optional[DTOConstant.StandardText]
    description_ru: DTOConstant.StandardText
    description_kk: DTOConstant.StandardText
    description_en: Optional[DTOConstant.StandardText]
    learned_after_course_ru: DTOConstant.StandardText
    learned_after_course_kk: DTOConstant.StandardText
    learned_after_course_en: Optional[DTOConstant.StandardText]
    price: int = Field(default=None, description="Стоимость курса")
    thumbnail: Optional[DTOConstant.StandardValue]
    author: Optional[DTOConstant.StandardValue]
    type_id: int = Field(default=None, description="Уникальный ID типа курса")
    category_id: int = Field(default=None, description="Уникальный ID категории курса")

