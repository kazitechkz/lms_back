from typing import Optional, List

from pydantic import BaseModel, Field

from app.infrastructure.db_constants import DTOConstant


class QuestionAttemptDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class QuestionAttemptRDTO(QuestionAttemptDTO):
    id: DTOConstant.StandardID
    user_id: DTOConstant.StandardID
    test_id: DTOConstant.StandardID
    question_id: DTOConstant.StandardID
    answer_id: Optional[int] = Field(default=None, description="ID ответа")
    is_correct: DTOConstant.StandardNullableBoolean
    point: int = Field(description="Баллы")

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class QuestionAttemptCDTO(BaseModel):
    user_id: DTOConstant.StandardID
    test_id: DTOConstant.StandardID
    question_id: DTOConstant.StandardID
    answer_id: Optional[int] = Field(default=None, description="ID ответа")
    is_correct: DTOConstant.StandardNullableBoolean
    point: int = Field(description="Баллы")

    class Config:
        from_attributes = True


class SingleAnswerCDTO(BaseModel):
    question_id: DTOConstant.StandardID
    answer_id: Optional[int] = Field(default=None, description="ID ответа")
    is_last: DTOConstant.StandardBoolean = False


class MultipleAnswerCDTO(BaseModel):
    question_id: DTOConstant.StandardID
    answer_ids: List[DTOConstant.StandardID]

