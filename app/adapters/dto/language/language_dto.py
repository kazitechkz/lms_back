from pydantic import BaseModel

from app.infrastructure.db_constants import DTOConstant


class LanguageDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class LanguageRDTO(LanguageDTO):
    title: DTOConstant.StandardVarchar
    value: DTOConstant.StandardValue
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

class LanguageCDTO(BaseModel):
    title: DTOConstant.StandardVarchar
    value: DTOConstant.StandardValue