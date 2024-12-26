from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class CourseCategoryModel(Base):
    __tablename__ = AppTableNames.CourseCategoryTableName
    id: Mapped[ColumnConstants.ID]
    title_ru: Mapped[ColumnConstants.StandardVarchar]
    title_kk: Mapped[ColumnConstants.StandardVarchar]
    title_en: Mapped[ColumnConstants.StandardNullableVarchar]
    value: Mapped[ColumnConstants.StandardUniqueValue]
    parent_id: Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.CourseCategoryTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]

    parent: Mapped["CourseCategoryModel"] = relationship(
        f"{AppTableNames.CourseCategoryModelName}",
        remote_side=f"{AppTableNames.CourseCategoryModelName}.id",
        back_populates="children",
    )
    children: Mapped[list["CourseCategoryModel"]] = relationship(
        f"{AppTableNames.CourseCategoryModelName}",
        back_populates="parent"
    )
