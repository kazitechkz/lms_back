from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.pagination_dto import PaginationQuestions
from app.adapters.dto.question.question_dto import QuestionRDTOWithRelated
from app.adapters.filters.question.question_filter import QuestionFilter
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.use_cases.base_case import BaseUseCase


class AllQuestionsCase(BaseUseCase[PaginationQuestions]):
    def __init__(self, db: AsyncSession):
        self.repository = QuestionRepository(db)

    async def execute(self, params: QuestionFilter):
        tests = await self.repository.paginate(
            dto=QuestionRDTOWithRelated,
            page=params.page,
            per_page=params.per_page,
            filters=params.apply(),
            options=[
                joinedload(self.repository.model.type),
                joinedload(self.repository.model.test),
            ]
        )
        return tests

    async def validate(self):
        pass
