from typing import Optional, List

from pydantic import BaseModel, Field

from app.infrastructure.db_constants import DTOConstant


class TestAttemptDTO(BaseModel):
    id: DTOConstant.StandardID

    class Config:
        from_attributes = True


class TestAttemptRDTO(TestAttemptDTO):
    id: DTOConstant.StandardID
    user_id: DTOConstant.StandardID
    test_id: DTOConstant.StandardID
    is_success: DTOConstant.StandardBoolean
    point: int = Field(description="Баллы")

    created_at: DTOConstant.StandardCreatedAt
    updated_at: DTOConstant.StandardUpdatedAt

    class Config:
        from_attributes = True


class TestAttemptCDTO(BaseModel):
    user_id: DTOConstant.StandardID
    test_id: DTOConstant.StandardID
    is_success: DTOConstant.StandardBoolean
    point: int = Field(description="Баллы")

    class Config:
        from_attributes = True

