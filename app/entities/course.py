from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class CourseModel(Base):
    __tablename__ = AppTableNames.CourseTableName
    id: Mapped[ColumnConstants.ID]
    title_ru: Mapped[ColumnConstants.StandardVarchar]
    title_kk: Mapped[ColumnConstants.StandardVarchar]
    title_en: Mapped[ColumnConstants.StandardNullableVarchar]
    short_description_kk: Mapped[ColumnConstants.StandardText]
    short_description_ru: Mapped[ColumnConstants.StandardText]
    short_description_en: Mapped[ColumnConstants.StandardNullableText]
    description_kk: Mapped[ColumnConstants.StandardText]
    description_ru: Mapped[ColumnConstants.StandardText]
    description_en: Mapped[ColumnConstants.StandardNullableText]
    learned_after_course_kk: Mapped[ColumnConstants.StandardText]
    learned_after_course_ru: Mapped[ColumnConstants.StandardText]
    learned_after_course_en: Mapped[ColumnConstants.StandardNullableText]
    thumbnail: Mapped[ColumnConstants.StandardNullableVarchar]
    author: Mapped[ColumnConstants.StandardNullableVarchar]

    category_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.CourseCategoryTableName,
        onupdate="CASCADE",
        ondelete="CASCADE"
    )]
    type_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.CourseTypeTableName,
        onupdate="CASCADE",
        ondelete="CASCADE"
    )]

    category: Mapped["CourseCategoryModel"] = relationship("CourseCategoryModel")
    type: Mapped["CourseTypeModel"] = relationship("CourseTypeModel")

    # materials: Mapped[list["MaterialModel"]] = relationship(
    #     f"{AppTableNames.MaterialModelName}",
    #     back_populates="parent"
    # )

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]


class CourseTagModel(Base):
    __tablename__ = AppTableNames.CourseTagTableName
    id: Mapped[ColumnConstants.ID]

    course_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.CourseTableName,
        onupdate="CASCADE",
        ondelete="CASCADE"
    )]
    tag_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.TagTableName,
        onupdate="CASCADE",
        ondelete="CASCADE"
    )]

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
