from typing import Optional

from sqlalchemy import Float
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.infrastructure.database import Base
from app.infrastructure.db_constants import (AppTableNames, ColumnConstants)


class TestTypeModel(Base):
    __tablename__ = "test_types"
    id: Mapped[ColumnConstants.ID]
    title_ru: Mapped[ColumnConstants.StandardVarchar]
    title_kk: Mapped[ColumnConstants.StandardVarchar]
    title_en: Mapped[ColumnConstants.StandardNullableVarchar]
    value: Mapped[ColumnConstants.StandardUniqueValue]
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]


class TestModel(Base):
    __tablename__ = AppTableNames.TestTableName
    id: Mapped[ColumnConstants.ID]
    title: Mapped[ColumnConstants.StandardVarchar]
    description: Mapped[ColumnConstants.StandardNullableText]
    type_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.TestTypeTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    is_demo: Mapped[ColumnConstants.StandardBool]
    organization_id: Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.OrganizationTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    course_id: Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.CourseTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    video_id: Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.VideoCourseTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    time_limit: Mapped[ColumnConstants.StandardNullableInteger]
    pass_point: Mapped[ColumnConstants.StandardNullableInteger]
    questions: Mapped[list[AppTableNames.QuestionModelName]] = relationship(
        f"{AppTableNames.QuestionModelName}",
        back_populates="test",
        viewonly=True
    )

    type: Mapped[AppTableNames.TestTypeModelName] = relationship(AppTableNames.TestTypeModelName)
    organization: Mapped[AppTableNames.OrganizationModelName] = relationship(AppTableNames.OrganizationModelName)
    course: Mapped[AppTableNames.CourseModelName] = relationship(AppTableNames.CourseModelName, lazy="noload")
    video: Mapped[AppTableNames.VideoCourseModelName] = relationship(AppTableNames.VideoCourseModelName, lazy="noload")
    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]


class QuestionModel(Base):
    __tablename__ = AppTableNames.QuestionTableName
    id: Mapped[ColumnConstants.ID]
    test_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.TestTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    text: Mapped[ColumnConstants.StandardText]
    hint: Mapped[ColumnConstants.StandardNullableText]
    explanation: Mapped[ColumnConstants.StandardNullableText]
    type_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.QuestionTypeTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]
    points: Mapped[float] = mapped_column(Float, default=1.0)

    answers: Mapped[list[AppTableNames.AnswerModelName]] = relationship(AppTableNames.AnswerModelName,
                                                                        viewonly=True)
    test: Mapped[AppTableNames.TestModelName] = relationship(AppTableNames.TestModelName,
                                                             viewonly=True)
    type: Mapped[AppTableNames.QuestionTypeModelName] = relationship(AppTableNames.QuestionTypeModelName,
                                                                     viewonly=True)

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]


class AnswerModel(Base):
    __tablename__ = AppTableNames.AnswerTableName
    id: Mapped[ColumnConstants.ID]
    question_id: Mapped[ColumnConstants.ForeignKeyInteger(
        table_name=AppTableNames.QuestionTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Связь с вопросом
    text: Mapped[ColumnConstants.StandardText]  # Текст ответа
    is_correct: Mapped[ColumnConstants.StandardBool]  # Является ли ответ правильным
    characteristic_id: Mapped[ColumnConstants.ForeignKeyNullableInteger(
        table_name=AppTableNames.CharacteristicTableName,
        onupdate="CASCADE",
        ondelete="SET NULL"
    )]  # Связанная характеристика (например, Личная мотивация)
    points: Mapped[Optional[float]] = mapped_column(Float, default=0.0)  # Баллы, которые добавляет ответ
    question: Mapped[AppTableNames.QuestionModelName] = relationship(AppTableNames.QuestionModelName,
                                                                     viewonly=True)

    created_at: Mapped[ColumnConstants.CreatedAt]
    updated_at: Mapped[ColumnConstants.UpdatedAt]
