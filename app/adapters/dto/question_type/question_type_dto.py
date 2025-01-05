from pydantic import BaseModel

from app.infrastructure.db_constants import DTOConstant


class QuestionTypeDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class QuestionTypeRDTO(QuestionTypeDTO):
    id: DTOConstant.StandardID
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    value: DTOConstant.StandardValue

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True
