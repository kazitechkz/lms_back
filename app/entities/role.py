from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants,
                                             FieldConstants)


class RoleModel(Base):
    __tablename__ = AppTableNames.RoleTableName
    id: Mapped[ColumnConstants.ID]
    title_ru: Mapped[ColumnConstants.StandardVarchar]
    title_kk: Mapped[ColumnConstants.StandardVarchar]
    title_en: Mapped[ColumnConstants.StandardNullableVarchar]
    value: Mapped[ColumnConstants.StandardUniqueValue]
    can_register: Mapped[bool] = mapped_column(default=True)
    is_admin: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]

    role_permissions: Mapped[list[AppTableNames.RolePermissionModelName]] = (
        relationship(
            AppTableNames.RolePermissionModelName,
            back_populates="role",
            cascade="all, delete-orphan",
            lazy="noload"
        )
    )
    users: Mapped[List[AppTableNames.UserModelName]] = relationship(
        AppTableNames.UserModelName, back_populates="role", cascade="all, delete-orphan"
    )
