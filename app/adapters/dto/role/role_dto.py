from typing import Optional

from pydantic import BaseModel, Field

from app.adapters.dto.role_permission.role_permission_dto import RolePermissionRDTOWithRelated
from app.infrastructure.db_constants import DTOConstant


class RoleDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class RoleRDTO(RoleDTO):
    id: DTOConstant.StandardID
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    value: DTOConstant.StandardValue
    can_register: bool = Field(
        default=True, description="Может ли роль регистрироваться"
    )
    is_admin: bool = Field(
        default=False, description="Является ли роль административной"
    )
    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class RoleCDTO(BaseModel):
    title_ru: DTOConstant.StandardTitleRu
    title_kk: DTOConstant.StandardTitleKk
    title_en: DTOConstant.StandardTitleEn
    value: DTOConstant.StandardValue
    can_register: bool = Field(
        default=False, description="Может ли роль регистрироваться"
    )
    is_admin: bool = Field(
        default=False, description="Является ли роль административной"
    )

    class Config:
        from_attributes = True


class RoleRDTOWithRelated(RoleRDTO):
    role_permissions: Optional[list[RolePermissionRDTOWithRelated]]

    class Config:
        from_attributes = True
