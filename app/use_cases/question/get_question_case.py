from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.question.question_dto import QuestionRDTO, QuestionRDTOWithRelated
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetQuestionCase(BaseUseCase[QuestionRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = QuestionRepository(db)

    async def execute(self, question_id: int) -> QuestionRDTOWithRelated:
        question = await self.validate(question_id=question_id)
        return QuestionRDTOWithRelated.from_orm(question)

    async def validate(self, question_id: int):
        question = await self.repository.get(question_id, options=[
            joinedload(self.repository.model.type),
            joinedload(self.repository.model.test)
        ])
        if not question:
            raise AppExceptionResponse.not_found("Вопрос не найден")
        return question
