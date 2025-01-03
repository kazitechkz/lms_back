from sqlalchemy import Column, Float
from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class AnswerModel(Base):
    __tablename__ = AppTableNames.AnswerTableName
    id = Mapped[ColumnConstants.ID]
    question_id = Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.QuestionTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Связь с вопросом
    text = Mapped[ColumnConstants.StandardVarchar]  # Текст ответа
    is_correct = Mapped[ColumnConstants.StandardBool]  # Является ли ответ правильным
    characteristic_id = Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.CharacteristicTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Связанная характеристика (например, Личная мотивация)
    points = Column(Float, default=0.0)  # Баллы, которые добавляет ответ
    question = relationship(AppTableNames.QuestionModelName, back_populates="answers")

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
