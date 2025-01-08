from sqlalchemy.orm import Mapped

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class TestAttemptModel(Base):
    __tablename__ = AppTableNames.TestAttemptTableName
    id: Mapped[ColumnConstants.ID]
    user_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.UserTableName,
    )]
    test_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.TestTableName
    )]
    point: Mapped[ColumnConstants.StandardInteger]
    is_success: Mapped[ColumnConstants.StandardBool]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
