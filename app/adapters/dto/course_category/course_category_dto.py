from typing import ForwardRef, Optional, List

from pydantic import BaseModel, Field

from app.infrastructure.db_constants import DTOConstant

# Объявление отложенной ссылки
CourseCategoryRef = ForwardRef("CourseCategoryRDTO")


class CourseCategoryDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class CourseCategoryRDTO(CourseCategoryDTO):
    id: DTOConstant.StandardID
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    value: DTOConstant.StandardValue
    parent_id: int | None = Field(default=None, description="Родительская категория")

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class CourseCategoryCDTO(BaseModel):
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    value: DTOConstant.StandardValue
    parent_id: int | None = Field(default=None, description="Родительская категория")


# Разрешение отложенной ссылки
CourseCategoryRDTO.update_forward_refs()


class CourseCategoryRDTOWithRelated(CourseCategoryRDTO):
    parent: Optional[CourseCategoryRef] = None
    children: Optional[List[CourseCategoryRef]] = Field(default=None, description="Дочерние категории")

    class Config:
        from_attributes = True
        validate_assignment = True
        arbitrary_types_allowed = True
        recursion_limit = 2

    @classmethod
    def from_orm_with_depth(cls, obj, depth: int = 1):
        """Создание DTO с ограничением глубины вложенности."""
        if depth == 0:
            return cls(
                id=obj.id,
                title_ru=obj.title_ru,
                title_kk=obj.title_kk,
                title_en=obj.title_en,
                value=obj.value,
                parent_id=obj.parent_id,
                created_at=obj.created_at,
                updated_at=obj.updated_at,
            )

        return cls(
            id=obj.id,
            title_ru=obj.title_ru,
            title_kk=obj.title_kk,
            title_en=obj.title_en,
            value=obj.value,
            parent_id=obj.parent_id,
            parent=cls.from_orm_with_depth(obj.parent, depth=depth - 1) if obj.parent else None,
            children=[
                cls.from_orm_with_depth(child, depth=depth - 1)
                for child in obj.children
            ] if obj.children else None,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
        )
