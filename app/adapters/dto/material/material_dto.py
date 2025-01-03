from pydantic import BaseModel, Field

from app.adapters.dto.file.file_dto import FileRDTO
from app.infrastructure.db_constants import DTOConstant


class MaterialDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class MaterialRDTO(MaterialDTO):
    id: DTOConstant.StandardID
    title: DTOConstant.StandardVarchar
    file_id: int | None = Field(default=None, description="Уникальный ID файла пользователя")
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class MaterialCDTO(BaseModel):
    title: DTOConstant.StandardVarchar
    file_id: int | None = Field(default=None, description="Уникальный ID файла пользователя")

    class Config:
        from_attributes = True


class MaterialRDTOWithRelated(MaterialRDTO):
    file: FileRDTO
