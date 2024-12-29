from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class CourseModel(Base):
    __tablename__ = AppTableNames.CourseTableName
    id: Mapped[ColumnConstants.ID]
    title: Mapped[ColumnConstants.StandardVarchar]
    short_description: Mapped[ColumnConstants.StandardNullableText]
    description: Mapped[ColumnConstants.StandardText]
    learned: Mapped[ColumnConstants.StandardText]
    price: Mapped[ColumnConstants.StandardInteger]
    thumbnail: Mapped[ColumnConstants.StandardNullableVarchar]
    author: Mapped[ColumnConstants.StandardNullableVarchar]

    lang_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.LanguageTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    category_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.CourseCategoryTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    type_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.CourseTypeTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]

    category: Mapped[AppTableNames.CourseCategoryModelName] = relationship(AppTableNames.CourseCategoryModelName)
    type: Mapped[AppTableNames.CourseTypeModelName] = relationship(AppTableNames.CourseTypeModelName)
    lang: Mapped[AppTableNames.LanguageModelName] = relationship(AppTableNames.LanguageModelName)

    tags: Mapped[list[AppTableNames.CourseTagModelName]] = relationship(
        f"{AppTableNames.CourseTagModelName}",
        )
    # materials: Mapped[list["MaterialModel"]] = relationship(
    #     f"{AppTableNames.MaterialModelName}",
    #     back_populates="parent"
    # )

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]


# class CourseMaterialModel(Base):
#     __tablename__ = AppTableNames.CourseMaterialTableName
#     id: Mapped[ColumnConstants.ID]
#
#     course_id: Mapped[ColumnConstants.ForeignKeyInteger(
#         table_name=AppTableNames.CourseTableName,
#         onupdate="CASCADE",
#         ondelete="CASCADE"
#     )]
#     material_id: Mapped[ColumnConstants.ForeignKeyInteger(
#         table_name=AppTableNames.TagTableName,
#         onupdate="CASCADE",
#         ondelete="CASCADE"
#     )]
#
#     created_at: Mapped[ColumnConstants.CreatedAt]
#     updated_at: Mapped[ColumnConstants.UpdatedAt]
