from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question_type.question_type_dto import QuestionTypeRDTO, QuestionTypeCDTO
from app.adapters.repositories.question_type.question_type_repository import QuestionTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateQuestionTypeCase(BaseUseCase[QuestionTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = QuestionTypeRepository(db)

    async def execute(self, dto: QuestionTypeCDTO) -> QuestionTypeRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return QuestionTypeRDTO.from_orm(data)

    async def validate(self, dto: QuestionTypeCDTO):
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Тип с таким значением уже существует"
            )
        return self.repository.model(**dto.dict())
