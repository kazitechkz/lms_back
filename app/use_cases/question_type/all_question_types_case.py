from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question_type.question_type_dto import QuestionTypeRDTO
from app.adapters.repositories.question_type.question_type_repository import QuestionTypeRepository
from app.use_cases.base_case import BaseUseCase


class AllQuestionTypesCase(BaseUseCase[List[QuestionTypeRDTO]]):
    def __init__(self, db: AsyncSession):
        self.repository = QuestionTypeRepository(db)

    async def execute(self) -> List[QuestionTypeRDTO]:
        question_types = await self.repository.get_all()
        return [QuestionTypeRDTO.from_orm(question_type) for question_type in question_types]

    async def validate(self):
        pass
