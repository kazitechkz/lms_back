from typing import Optional

from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.entities.course_material import CourseMaterialModel
from app.entities.video_courses import VideoCourseModel
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
    thumbnail: Mapped[str | None] = mapped_column(nullable=True)
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
    materials: Mapped[list[CourseMaterialModel]] = relationship(
        f"{AppTableNames.CourseMaterialModelName}",
        viewonly=True
    )
    video_courses: Mapped[list[VideoCourseModel]] = relationship(
        f"{AppTableNames.VideoCourseModelName}",
        viewonly=True
    )
    tags: Mapped[list[AppTableNames.CourseTagModelName]] = relationship(
        f"{AppTableNames.CourseTagModelName}",
    )

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
