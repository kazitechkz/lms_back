from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


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

    tag: Mapped[AppTableNames.TagModelName] = relationship(AppTableNames.TagModelName)

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
