from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question_type.question_type_dto import QuestionTypeRDTO
from app.adapters.repositories.question_type.question_type_repository import QuestionTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetQuestionTypeCase(BaseUseCase[QuestionTypeRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = QuestionTypeRepository(db)

    async def execute(self, question_type_id: int) -> QuestionTypeRDTO:
        question_type = await self.validate(question_type_id=question_type_id)
        return QuestionTypeRDTO.from_orm(question_type)

    async def validate(self, question_type_id: int):
        question_type = await self.repository.get(question_type_id)
        if not question_type:
            raise AppExceptionResponse.not_found("Тип не найден")
        return question_type
