from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class MaterialModel(Base):
    __tablename__ = AppTableNames.MaterialTableName
    id: Mapped[ColumnConstants.ID]
    title: Mapped[ColumnConstants.StandardVarchar]
    file_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.FileTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]

    file: Mapped[AppTableNames.FileModelName] = relationship(AppTableNames.FileModelName)

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
