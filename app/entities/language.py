from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (
    AppTableNames,
    ColumnConstants,
    FieldConstants,
)


class LanguageModel(Base):
    __tablename__ = AppTableNames.LanguageTableName
    id: Mapped[ColumnConstants.ID]
    title: Mapped[ColumnConstants.StandardVarchar]
    value: Mapped[ColumnConstants.StandardUniqueValue]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
