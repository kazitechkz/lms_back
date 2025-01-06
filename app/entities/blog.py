from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class BlogModel(Base):
    __tablename__ = AppTableNames.BlogTableName
    id: Mapped[ColumnConstants.ID]
    title: Mapped[ColumnConstants.StandardVarchar]
    short_description: Mapped[ColumnConstants.StandardNullableText]
    description: Mapped[ColumnConstants.StandardText]
    thumbnail: Mapped[ColumnConstants.StandardNullableText]
    author: Mapped[ColumnConstants.StandardNullableVarchar]
    status: Mapped[ColumnConstants.StandardBool]
    lang_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.LanguageTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    category_id: Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.BlogCategoryTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]

    lang: Mapped[AppTableNames.LanguageModelName] = relationship(
        AppTableNames.LanguageModelName
    )
    category: Mapped[AppTableNames.BlogCategoryModelName] = relationship(
        AppTableNames.BlogCategoryModelName
    )
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
