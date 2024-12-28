from pydantic import BaseModel, Field

from app.adapters.dto.permission.permission_dto import PermissionRDTO
from app.infrastructure.db_constants import DTOConstant


class RolePermissionDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class RolePermissionRDTO(RolePermissionDTO):
    id: DTOConstant.StandardID
    role_id: int = Field(description="Role ID")
    permission_id: int = Field(description="Permission ID")

    class Config:
        from_attributes = True


class RolePermissionCDTO(BaseModel):
    role_id: int = Field(description="Role ID")
    permission_id: int = Field(description="Permission ID")


class RolePermissionRDTOWithRelated(RolePermissionRDTO):
    permission: PermissionRDTO
