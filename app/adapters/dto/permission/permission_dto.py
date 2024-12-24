from pydantic import BaseModel, Field

from app.infrastructure.db_constants import DTOConstant


class PermissionDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class PermissionRDTO(PermissionDTO):
    id: DTOConstant.StandardID
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    value: DTOConstant.StandardValue
    description: DTOConstant.StandardText
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class PermissionCDTO(BaseModel):
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    value: DTOConstant.StandardValue
    description: DTOConstant.StandardText
