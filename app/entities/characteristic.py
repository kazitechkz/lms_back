from sqlalchemy.orm import Mapped

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class CharacteristicModel(Base):
    __tablename__ = AppTableNames.CharacteristicTableName
    id: Mapped[ColumnConstants.ID]
    title_ru: Mapped[ColumnConstants.StandardVarchar]
    title_kk: Mapped[ColumnConstants.StandardVarchar]
    title_en: Mapped[ColumnConstants.StandardNullableVarchar]
    description_ru: Mapped[ColumnConstants.StandardNullableText]
    description_kk: Mapped[ColumnConstants.StandardNullableText]
    description_en: Mapped[ColumnConstants.StandardNullableText]
    value: Mapped[ColumnConstants.StandardUniqueValue]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
