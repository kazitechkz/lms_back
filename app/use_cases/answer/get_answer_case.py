from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.answer.answer_dto import AnswerRDTO
from app.adapters.repositories.answer.answer_repository import AnswerRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetAnswerCase(BaseUseCase[AnswerRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = AnswerRepository(db)

    async def execute(self, answer_id: int) -> AnswerRDTO:
        answer = await self.validate(answer_id=answer_id)
        return AnswerRDTO.from_orm(answer)

    async def validate(self, answer_id: int):
        answer = await self.repository.get(answer_id)
        if not answer:
            raise AppExceptionResponse.not_found("Ответ не найден")
        return answer
