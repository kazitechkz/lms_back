from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.answer.answer_dto import AnswerCDTO, AnswerRDTO
from app.adapters.repositories.answer.answer_repository import AnswerRepository
from app.adapters.repositories.characteristic.characteristic_repository import CharacteristicRepository
from app.adapters.repositories.question.question_repository import QuestionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateAnswerCase(BaseUseCase[AnswerRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = AnswerRepository(db)
        self.question_repository = QuestionRepository(db)
        self.characteristic_repository = CharacteristicRepository(db)

    async def execute(self, id: int, dto: AnswerCDTO) -> AnswerRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return AnswerRDTO.from_orm(data)

    async def validate(self, id: int, dto: AnswerCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Ответ не найден")
        if await self.question_repository.get(id=dto.question_id) is None:
            raise AppExceptionResponse.bad_request(message="Вопрос не найден")
        if dto.characteristic_id:
            if await self.characteristic_repository.get(id=dto.characteristic_id) is None:
                raise AppExceptionResponse.bad_request(message="Характеристика не найдена")
        return existed