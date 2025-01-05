from typing import Optional

from pydantic import BaseModel, Field
from sqlalchemy import Float

from app.adapters.dto.question_type.question_type_dto import QuestionTypeRDTO
from app.adapters.dto.test.test_dto import TestRDTO
from app.infrastructure.db_constants import DTOConstant


class QuestionDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class QuestionRDTO(QuestionDTO):
    id: DTOConstant.StandardID
    test_id: DTOConstant.StandardID
    text: DTOConstant.StandardText
    hint: Optional[DTOConstant.StandardText]
    explanation: Optional[DTOConstant.StandardText]
    type_id: DTOConstant.StandardID
    points: Optional[float] = Field(description="Баллы")

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class QuestionCDTO(BaseModel):
    test_id: DTOConstant.StandardID
    text: DTOConstant.StandardText
    hint: Optional[DTOConstant.StandardText]
    explanation: Optional[DTOConstant.StandardText]
    type_id: DTOConstant.StandardID
    points: Optional[float] = Field(description="Баллы")

    class Config:
        from_attributes = True


class QuestionUDTO(BaseModel):
    test_id: Optional[DTOConstant.StandardID]
    text: Optional[DTOConstant.StandardText]
    hint: Optional[DTOConstant.StandardText]
    explanation: Optional[DTOConstant.StandardText]
    type_id: Optional[DTOConstant.StandardID]
    points: float = Optional[Field(description="Баллы")]


class QuestionRDTOWithRelated(QuestionRDTO):
    type: QuestionTypeRDTO
    test: TestRDTO
