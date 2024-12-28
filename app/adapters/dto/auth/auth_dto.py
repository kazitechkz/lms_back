from pydantic import BaseModel, EmailStr, Field

from app.infrastructure.db_constants import DTOConstant


class AuthDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class AuthCDTO(BaseModel):
    email: EmailStr = Field(description="Email")
    password: str = Field(description="Пароль", min_length=4)

    class Config:
        from_attributes = True


class AuthRDTO(BaseModel):
    access_token: DTOConstant.StandardVarchar
    refresh_token: DTOConstant.StandardVarchar
    token_type: DTOConstant.StandardVarchar

    class Config:
        from_attributes = True
