from typing import Optional

from pydantic import BaseModel, Field

from app.adapters.dto.blog_category.blog_category_dto import BlogCategoryRDTO
from app.adapters.dto.language.language_dto import LanguageRDTO
from app.infrastructure.db_constants import DTOConstant


class BlogDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class BlogRDTO(BlogDTO):
    id: DTOConstant.StandardID
    title: DTOConstant.StandardTitleRu
    short_description: Optional[DTOConstant.StandardText]
    description: DTOConstant.StandardText
    thumbnail: str | None = Field(default=None, description="Обложка блога")
    author: DTOConstant.StandardValue
    status: DTOConstant.StandardBoolean
    category_id: int | None = Field(default=None, description="Уникальный ID категории блога")
    lang_id: int = Field(description="Уникальный ID языка")

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class BlogCDTO(BaseModel):
    title: DTOConstant.StandardTitleRu
    short_description: Optional[DTOConstant.StandardText]
    description: DTOConstant.StandardText
    thumbnail: str | None = Field(default=None, description="Обложка блога")
    author: DTOConstant.StandardValue
    status: DTOConstant.StandardBoolean
    category_id: int | None = Field(default=None, description="Уникальный ID категории блога")
    lang_id: int = Field(description="Уникальный ID языка")

    class Config:
        from_attributes = True


class BlogRDTOWithRelated(BlogRDTO):
    category: Optional[BlogCategoryRDTO] = Field(default=None, description="Категория блога")
    lang: Optional[LanguageRDTO] = Field(default=None, description="Язык блога")

    class Config:
        from_attributes = True
