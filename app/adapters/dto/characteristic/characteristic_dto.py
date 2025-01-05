from typing import Optional

from pydantic import BaseModel

from app.infrastructure.db_constants import DTOConstant


class CharacteristicDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class CharacteristicRDTO(CharacteristicDTO):
    id: DTOConstant.StandardID
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    description_kk: DTOConstant.StandardText
    description_ru: DTOConstant.StandardText
    description_en: Optional[DTOConstant.StandardText]
    value: DTOConstant.StandardValue

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class CharacteristicCDTO(BaseModel):
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    description_kk: DTOConstant.StandardText
    description_ru: DTOConstant.StandardText
    description_en: Optional[DTOConstant.StandardText]
    value: DTOConstant.StandardValue

    class Config:
        from_attributes = True

