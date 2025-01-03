from pydantic import BaseModel

from app.adapters.dto.organization_type.organization_type_dto import OrganizationTypeRDTO
from app.infrastructure.db_constants import DTOConstant


class OrganizationDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class OrganizationRDTO(OrganizationDTO):
    id: DTOConstant.StandardID
    name: DTOConstant.StandardVarchar
    description: DTOConstant.StandardText
    bin: DTOConstant.StandardText
    type_id: DTOConstant.StandardInteger

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class OrganizationCDTO(BaseModel):
    name: DTOConstant.StandardVarchar
    description: DTOConstant.StandardText
    bin: DTOConstant.StandardText
    type_id: DTOConstant.StandardInteger

    class Config:
        from_attributes = True


class OrganizationRDTOWithRelated(OrganizationRDTO):
    type: OrganizationTypeRDTO
