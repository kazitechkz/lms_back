from pydantic import BaseModel, Field

from app.infrastructure.db_constants import DTOConstant


class FileDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class FileRDTO(FileDTO):
    id: DTOConstant.StandardID
    filename: DTOConstant.StandardVarchar
    file_path: DTOConstant.StandardText
    file_size: int = Field(description="Размер файла")
    content_type: DTOConstant.StandardVarchar
    is_active: bool = Field(description="Статус файла")
    uploaded_by: int = Field(description="Уникальный ID пользователя")
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class FileCDTO(BaseModel):
    filename: DTOConstant.StandardVarchar
    file_path: DTOConstant.StandardText
    file_size: int = Field(description="Размер файла")
    content_type: DTOConstant.StandardVarchar
    is_active: bool = Field(description="Статус файла")
    uploaded_by: int = Field(description="Уникальный ID пользователя")

    class Config:
        from_attributes = True
