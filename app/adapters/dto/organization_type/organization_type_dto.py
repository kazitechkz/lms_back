from pydantic import BaseModel

from app.infrastructure.db_constants import DTOConstant


class OrganizationTypeDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class OrganizationTypeRDTO(OrganizationTypeDTO):
    id: DTOConstant.StandardID
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    value: DTOConstant.StandardValue

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class OrganizationTypeCDTO(BaseModel):
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn

    class Config:
        from_attributes = True
