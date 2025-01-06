from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.feedback.feedback_dto import FeedbackCDTO, FeedbackRDTOWithRelated
from app.adapters.repositories.feedback.feedback_repository import FeedbackRepository
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.adapters.repositories.test.test_repository import TestRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateFeedbackCase(BaseUseCase[FeedbackRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = FeedbackRepository(db)
        self.test_repository = TestRepository(db)
        self.question_repository = QuestionRepository(db)

    async def execute(self, id: int, dto: FeedbackCDTO) -> FeedbackRDTOWithRelated:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto, options=[
            joinedload(self.repository.model.test),
            joinedload(self.repository.model.question)
        ])
        return FeedbackRDTOWithRelated.from_orm(data)

    async def validate(self, id: int, dto: FeedbackCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Обращение не найдено")
        if await self.test_repository.get(id=dto.test_id) is None:
            raise AppExceptionResponse.bad_request(message="Тест не найден")
        if dto.question_id:
            if await self.question_repository.get(id=dto.question_id) is None:
                raise AppExceptionResponse.bad_request(message="Вопрос не найден")
        return existed
