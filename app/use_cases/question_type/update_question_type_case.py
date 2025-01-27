from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question_type.question_type_dto import QuestionTypeRDTO, QuestionTypeCDTO
from app.adapters.repositories.question_type.question_type_repository import QuestionTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateQuestionTypeCase(BaseUseCase[QuestionTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = QuestionTypeRepository(db)

    async def execute(self, id: int, dto: QuestionTypeCDTO) -> QuestionTypeRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return QuestionTypeRDTO.from_orm(data)

    async def validate(self, id: int, dto: QuestionTypeCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Тип не найден")
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value, self.repository.model.id != id]
        ):
            raise AppExceptionResponse.bad_request(
                "Тип с таким значением уже существует"
            )
        return existed
