from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.auth.auth_dto import AuthRDTO, AuthCDTO
from app.adapters.repositories.auth.auth_repository import AuthRepository
from app.core.app_exception_response import AppExceptionResponse
from app.core.auth_core import verify_password, create_access_token, create_refresh_token
from app.use_cases.base_case import BaseUseCase


class AuthLoginUseCase(BaseUseCase[AuthRDTO]):
    def __init__(self, db: AsyncSession):
        self.repo = AuthRepository(db)

    async def execute(self, dto: AuthCDTO) -> AuthRDTO:
        return await self.validate(dto=dto)

    async def validate(self, dto: AuthCDTO):
        user = await self.repo.get_first_with_filters(filters=[
            and_(self.repo.model.email == dto.email)
        ])
        if user is None:
            raise AppExceptionResponse.bad_request(message="Пользователь с такой почтой не найден")

        result = verify_password(dto.password, user.password_hash)
        if not result:
            raise AppExceptionResponse.bad_request(message="Неверный пароль")

        access_token = create_access_token(data=user.id)
        refresh_token = create_refresh_token(data=user.id)

        return AuthRDTO(
            access_token=access_token,
            refresh_token=refresh_token
        )
