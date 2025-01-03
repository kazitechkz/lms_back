from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class VideoMaterialModel(Base):
    __tablename__ = AppTableNames.VideoMaterialTableName
    id: Mapped[ColumnConstants.ID]
    video_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.VideoCourseTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    material_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.MaterialTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]

    video: Mapped[AppTableNames.VideoCourseModelName] = relationship(AppTableNames.VideoCourseModelName)
    material: Mapped[AppTableNames.MaterialModelName] = relationship(AppTableNames.MaterialModelName)

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
