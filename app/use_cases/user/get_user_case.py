from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.repositories.user.user_repository import UserRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetUserCase(BaseUseCase[UserRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def execute(self, user_id: int) -> UserRDTOWithRelated:
        user = await self.validate(user_id=user_id)
        return UserRDTOWithRelated.from_orm(user)

    async def validate(self, user_id: int):
        user = await self.repository.get(user_id, options=[
                joinedload(self.repository.model.user_type),
                joinedload(self.repository.model.role),
                joinedload(self.repository.model.file),
            ])
        if not user:
            raise AppExceptionResponse.not_found("Пользователь не найден")
        return user
