from pydantic import BaseModel

from app.infrastructure.db_constants import DTOConstant


class TokenDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class TokenRDTO(TokenDTO):
    id: DTOConstant.StandardID
    access_token: DTOConstant.StandardText
    refresh_token: DTOConstant.StandardText

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class TokenCDTO(BaseModel):
    access_token: DTOConstant.StandardText
    refresh_token: DTOConstant.StandardText

    class Config:
        from_attributes = True

