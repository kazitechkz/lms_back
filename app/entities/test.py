import enum

from sqlalchemy import Column, Enum
from sqlalchemy.orm import Mapped, relationship

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class TestType(enum.Enum):
    TEST = "Тестовый"
    EXAM = "Экзаменационный"


class TestModel(Base):
    __tablename__ = AppTableNames.TestTableName
    id = Mapped[ColumnConstants.ID]
    title = Mapped[ColumnConstants.StandardVarchar]  # Название теста
    description = Mapped[ColumnConstants.StandardNullableText]  # Описание теста
    type = Column(Enum(TestType), nullable=False)  # Тип теста (Тестовый/Экзаменационный)
    is_demo = Mapped[ColumnConstants.StandardBool]  # Доступен ли тест как демо
    organization_id = Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.OrganizationTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Организация (если тест для организаций)
    course_id = Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.CourseTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Привязка к курсу (если есть)
    time_limit = Mapped[ColumnConstants.StandardNullableInteger]  # Ограничение по времени в минутах (для экзаменов)
    questions = relationship(AppTableNames.OrganizationModelName, back_populates="test")  # Связь с вопросами

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
