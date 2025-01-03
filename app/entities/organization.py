from sqlalchemy.orm import Mapped, relationship

from app.entities import OrganizationTypeModel
from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class OrganizationModel(Base):
    __tablename__ = AppTableNames.OrganizationTableName
    id: Mapped[ColumnConstants.ID]
    name: Mapped[ColumnConstants.StandardVarchar]
    bin: Mapped[ColumnConstants.StandardText]
    description: Mapped[ColumnConstants.StandardNullableText]
    type_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.OrganizationTypeTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]

    type: Mapped[OrganizationTypeModel] = relationship(
        AppTableNames.OrganizationTypeModelName
    )
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
