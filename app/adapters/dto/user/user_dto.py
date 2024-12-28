from pydantic import BaseModel, Field, EmailStr

from app.adapters.dto.file.file_dto import FileRDTO
from app.adapters.dto.role.role_dto import RoleRDTOWithRelated
from app.adapters.dto.user_type.user_type_dto import UserTypeRDTO
from app.infrastructure.db_constants import DTOConstant, FieldConstants


class UserDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class UserRDTO(UserDTO):
    id: DTOConstant.StandardID
    name: str = Field(description="ФИО пользователя", max_length=FieldConstants.STANDARD_LENGTH)
    email: EmailStr = Field(description="Email")
    phone: str = Field(description="Номер телефона", max_length=FieldConstants.STANDARD_LENGTH)
    position: str | None = Field(default=None, description="", max_length=FieldConstants.STANDARD_LENGTH)
    is_active: bool = Field(description="Статус пользователя", default=True)
    role_id: int = Field(description="Уникальный ID роли пользователя")
    user_type_id: int = Field(description="Уникальный ID типа пользователя")
    file_id: int | None = Field(default=None, description="Уникальный ID файла пользователя")
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class UserCDTO(BaseModel):
    name: str = Field(description="ФИО пользователя", max_length=FieldConstants.STANDARD_LENGTH)
    email: EmailStr = Field(description="Email")
    phone: str = Field(description="Номер телефона", max_length=FieldConstants.STANDARD_LENGTH)
    position: str | None = Field(default=None, description="", max_length=FieldConstants.STANDARD_LENGTH)
    password_hash: str = Field(
        description="Пароль пользователя", max_length=FieldConstants.STANDARD_LENGTH, min_length=4
    )
    is_active: bool = Field(description="Статус пользователя", default=True)
    role_id: int = Field(description="Уникальный ID роли пользователя")
    user_type_id: int = Field(description="Уникальный ID типа пользователя")
    file_id: int | None = Field(default=None, description="Уникальный ID файла пользователя")

    class Config:
        from_attributes = True


class UserRDTOWithRelated(UserRDTO):
    role: RoleRDTOWithRelated
    user_type: UserTypeRDTO
    file: FileRDTO | None = None

    class Config:
        from_attributes = True
