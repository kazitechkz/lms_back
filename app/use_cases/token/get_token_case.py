from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.dto.token.token_dto import TokenRDTO
from app.adapters.repositories.token.token_repository import TokenRepository
from app.entities.tokens import TokenModel
from app.use_cases.base_case import BaseUseCase


class GetTokenCase(BaseUseCase[RoleRDTO]):

    def __init__(self, db: AsyncSession):
        self.repository = TokenRepository(db)

    async def execute(self) -> TokenRDTO:
        token = await self.validate()
        return TokenRDTO.from_orm(token)

    async def validate(self):
        token = await self.repository.get(id=1)
        if not token:
            data = {
                "access_token": "test token",
                "refresh_token": "test refresh token",
            }
            token = await self.repository.create(obj=TokenModel(**data))
        return token
