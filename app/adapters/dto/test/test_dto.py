from typing import Optional

from pydantic import BaseModel, Field

from app.adapters.dto.test_type.tag_type_dto import TestTypeRDTO
from app.infrastructure.db_constants import DTOConstant


class TestDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class TestRDTO(TestDTO):
    id: DTOConstant.StandardID
    title: DTOConstant.StandardVarchar
    description: Optional[DTOConstant.StandardText]
    type_id: DTOConstant.StandardID
    is_demo: bool
    organization_id: Optional[int] = None
    course_id: Optional[int] = None
    video_id: Optional[int] = None
    time_limit: Optional[int] = None
    pass_point: Optional[int] = None

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class TestCDTO(BaseModel):
    title: str = Field(..., max_length=255, description="Название теста")
    description: Optional[str] = Field(None, description="Описание теста")
    type_id: int = Field(..., description="Тип теста (Тестовый или Экзаменационный)")
    is_demo: bool = Field(..., description="Доступен ли тест как демо")
    organization_id: Optional[int] = Field(None, description="ID организации, если тест привязан к организации")
    course_id: Optional[int] = Field(None, description="ID курса, если тест привязан к курсу")
    video_id: Optional[int] = Field(None, description="ID видеокурса, если тест привязан к видеокурсу")
    time_limit: Optional[int] = Field(None, ge=0, description="Ограничение по времени в минутах (0 для безлимита)")
    pass_point: Optional[int] = Field(None, ge=0, le=100, description="Проходной балл в процентах (от 0 до 100)")

    class Config:
        from_attributes = True


class TestUDTO(BaseModel):
    title: Optional[str] = Field(None, max_length=255, description="Название теста")
    description: Optional[str] = Field(None, description="Описание теста")
    type_id: Optional[int] = Field(None, description="Тип теста (Тестовый или Экзаменационный)")
    is_demo: Optional[bool] = Field(None, description="Доступен ли тест как демо")
    organization_id: Optional[int] = Field(None, description="ID организации, если тест привязан к организации")
    course_id: Optional[int] = Field(None, description="ID курса, если тест привязан к курсу")
    video_id: Optional[int] = Field(None, description="ID видеокурса, если тест привязан к видеокурсу")
    time_limit: Optional[int] = Field(None, ge=0, description="Ограничение по времени в минутах (0 для безлимита)")
    pass_point: Optional[int] = Field(None, ge=0, le=100, description="Проходной балл в процентах (от 0 до 100)")


class TestRDTOWithRelated(TestRDTO):
    type: TestTypeRDTO
