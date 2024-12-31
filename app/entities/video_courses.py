from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class VideoCourseModel(Base):
    __tablename__ = AppTableNames.VideoCourseTableName
    id: Mapped[ColumnConstants.ID]
    title: Mapped[ColumnConstants.StandardVarchar]
    video_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.FileTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    image: Mapped[ColumnConstants.StandardText]
    description: Mapped[ColumnConstants.StandardText]
    level: Mapped[ColumnConstants.StandardInteger]
    course_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.CourseTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    lang_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.LanguageTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]

    course: Mapped[AppTableNames.CourseModelName] = relationship(AppTableNames.CourseModelName)
    video: Mapped[AppTableNames.FileModelName] = relationship(AppTableNames.FileModelName)
    lang: Mapped[AppTableNames.LanguageModelName] = relationship(AppTableNames.LanguageModelName)

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
