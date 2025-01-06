from typing import Optional

from pydantic import BaseModel, Field

from app.infrastructure.db_constants import DTOConstant


class AnswerDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class AnswerRDTO(AnswerDTO):
    id: DTOConstant.StandardID
    question_id: DTOConstant.StandardID
    text: DTOConstant.StandardText
    is_correct: DTOConstant.StandardBoolean
    characteristic_id: DTOConstant.StandardNullableInteger
    points: float = Field(description="Баллы")

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class AnswerCDTO(BaseModel):
    question_id: DTOConstant.StandardID
    text: DTOConstant.StandardText
    is_correct: DTOConstant.StandardBoolean
    characteristic_id: Optional[DTOConstant.StandardNullableInteger]
    points: float = Field(default=0.0, description="Баллы")

    class Config:
        from_attributes = True

