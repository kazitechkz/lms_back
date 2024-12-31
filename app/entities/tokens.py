from sqlalchemy.orm import Mapped

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class TokenModel(Base):
    __tablename__ = AppTableNames.TokenTableName
    id: Mapped[ColumnConstants.ID]
    access_token: Mapped[ColumnConstants.StandardText]
    refresh_token: Mapped[ColumnConstants.StandardText]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
