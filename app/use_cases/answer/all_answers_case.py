from typing import List

from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.answer.answer_dto import AnswerRDTO
from app.adapters.repositories.answer.answer_repository import AnswerRepository
from app.use_cases.base_case import BaseUseCase


class AllAnswersCase(BaseUseCase[List[AnswerRDTO]]):
    def __init__(self, db: AsyncSession):
        self.repository = AnswerRepository(db)

    async def execute(self, question_id: int) -> List[AnswerRDTO]:
        answers = await self.repository.get_with_filters(filters=[
            and_(self.repository.model.question_id == question_id)
        ])
        return [AnswerRDTO.from_orm(answer) for answer in answers]

    async def validate(self):
        pass
