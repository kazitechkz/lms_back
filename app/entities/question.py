from sqlalchemy import Column, Float
from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class QuestionModel(Base):
    __tablename__ = AppTableNames.TestTableName
    id = Mapped[ColumnConstants.ID]
    test_id = Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.TestTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Связь с тестом
    text = Mapped[ColumnConstants.StandardText]  # Текст вопроса
    hint = Mapped[ColumnConstants.StandardNullableText]  # Подсказка (если есть)
    explanation = Mapped[ColumnConstants.StandardNullableText]  # Объяснение решения
    type_id = Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.QuestionTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Тип вопроса (верно/неверно, один/несколько ответов)
    points = Column(Float, default=1.0)  # Баллы за вопрос
    test = relationship(AppTableNames.TestModelName, back_populates="questions")  # Обратная связь с тестом
    answers = relationship(AppTableNames.AnswerModelName, back_populates="question")  # Связь с ответами
    
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
