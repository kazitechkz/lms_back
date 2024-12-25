from typing import Optional, List

from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import AppTableNames, ColumnConstants


class FileModel(Base):
    __tablename__ = AppTableNames.FileTableName
    id: Mapped[ColumnConstants.ID]
    filename: Mapped[ColumnConstants.StandardVarchar]
    file_path: Mapped[ColumnConstants.StandardText]
    file_size: Mapped[ColumnConstants.StandardInteger]
    content_type: Mapped[ColumnConstants.StandardVarchar]
    uploaded_by: Mapped[Optional[int]] = mapped_column(
        ForeignKey(f"{AppTableNames.UserTableName}.id", ondelete="SET NULL"),
        nullable=True,
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    uploaded_by_user: Mapped[Optional[AppTableNames.UserModelName]] = relationship(
        AppTableNames.UserModelName,
        foreign_keys=[uploaded_by],  # Явно указываем внешний ключ
        back_populates="uploaded_files",
    )
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]

    users: Mapped[List[AppTableNames.UserModelName]] = relationship(
        AppTableNames.UserModelName,
        foreign_keys=f"{AppTableNames.UserModelName}.file_id",  # Указываем, что связь через file_id
        back_populates="file",
    )
