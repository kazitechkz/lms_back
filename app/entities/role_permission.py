from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants,
                                             FieldConstants)


class RolePermissionModel(Base):
    __tablename__ = AppTableNames.RolePermissionTableName
    id: Mapped[ColumnConstants.ID]
    role_id: Mapped[int] = mapped_column(
        ForeignKey(f"{AppTableNames.RoleTableName}.id", ondelete="CASCADE")
    )
    role: Mapped[AppTableNames.RoleModelName] = relationship(
        AppTableNames.RoleModelName, back_populates="role_permissions"
    )
    permission_id: Mapped[int] = mapped_column(
        ForeignKey(f"{AppTableNames.PermissionTableName}.id", ondelete="CASCADE")
    )
    permission: Mapped[AppTableNames.PermissionModelName] = relationship(
        AppTableNames.PermissionModelName, back_populates="role_permissions"
    )
