from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question_type.question_type_dto import QuestionTypeRDTO
from app.adapters.repositories.question_type.question_type_repository import QuestionTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetQuestionTypeByValueCase(BaseUseCase[QuestionTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.question_type_repository = QuestionTypeRepository(db)

    async def execute(self, question_type_value: str) -> QuestionTypeRDTO:
        question_type = await self.validate(question_type_value=question_type_value)
        return QuestionTypeRDTO.from_orm(question_type)

    async def validate(self, question_type_value: str):
        filters = [self.question_type_repository.model.value == question_type_value]
        question_type = await self.question_type_repository.get_first_with_filters(filters)
        if not question_type:
            raise AppExceptionResponse.not_found("Тип не найден")
        return question_type
