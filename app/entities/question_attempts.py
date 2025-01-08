from sqlalchemy.orm import Mapped

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class QuestionAttemptModel(Base):
    __tablename__ = AppTableNames.QuestionAttemptTableName
    id: Mapped[ColumnConstants.ID]
    user_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.UserTableName,
    )]
    test_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.TestTableName
    )]
    question_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.QuestionTableName
    )]
    answer_id: Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.AnswerTableName
    )]
    is_correct: Mapped[ColumnConstants.StandardBool]
    point: Mapped[ColumnConstants.StandardInteger]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
