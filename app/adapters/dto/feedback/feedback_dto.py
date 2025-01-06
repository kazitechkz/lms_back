from typing import Optional

from pydantic import BaseModel

from app.adapters.dto.question.question_dto import QuestionRDTO
from app.adapters.dto.test.test_dto import TestRDTO
from app.infrastructure.db_constants import DTOConstant


class FeedbackDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class FeedbackRDTO(FeedbackDTO):
    id: DTOConstant.StandardID
    description: DTOConstant.StandardText
    test_id: DTOConstant.StandardInteger
    question_id: DTOConstant.StandardNullableInteger

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class FeedbackCDTO(BaseModel):
    description: DTOConstant.StandardText
    test_id: DTOConstant.StandardInteger
    question_id: DTOConstant.StandardNullableInteger

    class Config:
        from_attributes = True


class FeedbackRDTOWithRelated(FeedbackRDTO):
    test: TestRDTO
    question: Optional[QuestionRDTO]
