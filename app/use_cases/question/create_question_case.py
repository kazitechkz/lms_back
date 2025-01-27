from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.question.question_dto import QuestionRDTO, QuestionCDTO, QuestionRDTOWithRelated
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.adapters.repositories.test.test_repository import TestRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateQuestionCase(BaseUseCase[QuestionRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = QuestionRepository(db)
        self.test_repository = TestRepository(db)

    async def execute(self, dto: QuestionCDTO) -> QuestionRDTOWithRelated:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj, options=[
            selectinload(self.repository.model.type),
            selectinload(self.repository.model.test)
        ])
        return QuestionRDTOWithRelated.from_orm(data)

    async def validate(self, dto: QuestionCDTO):
        if await self.test_repository.get(id=dto.test_id) is None:
            raise AppExceptionResponse.bad_request(message="Тест не найден")
        if dto.type_id == 1:
            dto.points = 1
        # if dto.type_id == 2:
        #     if dto.points is None:
        #         raise AppExceptionResponse.bad_request(message="Не указано количество баллов")
        return self.repository.model(**dto.dict())
