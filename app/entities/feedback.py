from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class FeedbackModel(Base):
    __tablename__ = AppTableNames.FeedbackTableName
    id: Mapped[ColumnConstants.ID]
    description: Mapped[ColumnConstants.StandardText]  # Описание теста
    test_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.TestTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Тест, к которому относится ошибка
    question_id: Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.QuestionTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Вопрос, где найдена ошибка

    test: Mapped[AppTableNames.TestModelName] = relationship(AppTableNames.TestModelName)
    question: Mapped[AppTableNames.QuestionModelName] = relationship(AppTableNames.QuestionModelName)

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
