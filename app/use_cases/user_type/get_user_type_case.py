from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.user_type.user_type_dto import UserTypeRDTO
from app.adapters.repositories.user_type.user_type_repository import UserTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetUserTypeCase(BaseUseCase[UserTypeRDTO]):

    def __init__(self, db: AsyncSession):
        self.repo = UserTypeRepository(db)

    async def execute(self, user_type_id: int) -> UserTypeRDTO:
        user_type = await self.validate(user_type_id=user_type_id)
        return UserTypeRDTO.from_orm(user_type)

    async def validate(self, user_type_id: int):
        user_type = await self.repo.get(user_type_id)
        if not user_type:
            raise AppExceptionResponse.not_found("Тип пользователя не найден")
        return user_type
