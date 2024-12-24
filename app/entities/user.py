from typing import Optional, List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import AppTableNames, ColumnConstants


class UserModel(Base):
    __tablename__ = AppTableNames.UserTableName
    id: Mapped[ColumnConstants.ID]
    name: Mapped[ColumnConstants.StandardVarchar]
    email: Mapped[ColumnConstants.StandardUniqueEmail]
    phone: Mapped[ColumnConstants.StandardUniquePhone]
    position: Mapped[ColumnConstants.StandardNullableText]
    password_hash: Mapped[ColumnConstants.StandardText]
    is_active: Mapped[bool] = mapped_column(default=True)

    role_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(f"{AppTableNames.RoleTableName}.id", ondelete="SET NULL"),
        nullable=True,
    )
    role: Mapped[AppTableNames.RoleModelName] = relationship(
        AppTableNames.RoleModelName, back_populates="users"
    )
    user_type_id: Mapped[int] = mapped_column(
        ForeignKey(f"{AppTableNames.UserTypeTableName}.id", ondelete="SET NULL"),
        nullable=True,
    )
    user_type: Mapped[AppTableNames.UserTypeModelName] = relationship(
        AppTableNames.UserTypeModelName, back_populates="users"
    )
    file_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey(f"{AppTableNames.FileTableName}.id", ondelete="SET NULL"),
        nullable=True
    )
    file: Mapped[Optional[AppTableNames.FileModelName]] = relationship(
        AppTableNames.FileModelName,
        foreign_keys=[file_id],
        back_populates="users",
    )

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]

    uploaded_files: Mapped[List[AppTableNames.FileModelName]] = relationship(
        AppTableNames.FileModelName,
        foreign_keys=f"{AppTableNames.FileModelName}.uploaded_by",
        back_populates="uploaded_by_user",
        cascade="all, delete-orphan",
    )
