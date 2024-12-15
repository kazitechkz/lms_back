from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants,
                                             FieldConstants)


class UserTypeModel(Base):
    __tablename__ = AppTableNames.UserTypeTableName
    id: Mapped[ColumnConstants.ID]
    title_ru: Mapped[ColumnConstants.StandardVarchar]
    title_kk: Mapped[ColumnConstants.StandardVarchar]
    title_en: Mapped[ColumnConstants.StandardNullableVarchar]
    value: Mapped[ColumnConstants.StandardUniqueValue]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
