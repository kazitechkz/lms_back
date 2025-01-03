from sqlalchemy.orm import Mapped, relationship

from app.entities.material import MaterialModel
from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class CourseMaterialModel(Base):
    __tablename__ = AppTableNames.CourseMaterialTableName
    id: Mapped[ColumnConstants.ID]
    course_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.CourseTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    material_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.MaterialTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    material: Mapped[MaterialModel] = relationship(AppTableNames.MaterialModelName)
    course: Mapped[AppTableNames.CourseModelName] = relationship(AppTableNames.CourseModelName)

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
