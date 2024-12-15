from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import AppTableNames, ColumnConstants


class PermissionModel(Base):
    __tablename__ = AppTableNames.PermissionTableName
    id: Mapped[ColumnConstants.ID]
    title_ru: Mapped[ColumnConstants.StandardVarchar]
    title_kk: Mapped[ColumnConstants.StandardVarchar]
    title_en: Mapped[ColumnConstants.StandardNullableVarchar]
    value: Mapped[ColumnConstants.StandardUniqueValue]
    description: Mapped[ColumnConstants.StandardText]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]

    role_permissions: Mapped[list[AppTableNames.RolePermissionModelName]] = (
        relationship(
            AppTableNames.RolePermissionModelName,
            back_populates="permission",
            cascade="all, delete-orphan",
        )
    )
