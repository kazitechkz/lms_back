from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.user_type.user_type_dto import UserTypeRDTO
from app.adapters.repositories.user_type.user_type_repository import UserTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetUserTypeByValueCase(BaseUseCase[UserTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = UserTypeRepository(db)

    async def execute(self, user_type_value: str) -> UserTypeRDTO:
        user_type = await self.validate(user_type_value=user_type_value)
        return UserTypeRDTO.from_orm(user_type)

    async def validate(self, user_type_value: str):
        filters = [self.repository.model.value == user_type_value]
        user_type = await self.repository.get_first_with_filters(filters)
        if not user_type:
            raise AppExceptionResponse.not_found("Тип пользователя не найден")
        return user_type
