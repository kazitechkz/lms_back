from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.token.token_dto import TokenRDTO, TokenCDTO
from app.adapters.repositories.token.token_repository import TokenRepository
from app.use_cases.base_case import BaseUseCase


class UpdateTokenCase(BaseUseCase[TokenRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = TokenRepository(db)

    async def execute(self, access_token: str):
        await self.validate(access_token=access_token)
        return True

    async def validate(self, access_token: str):
        token = await self.repository.get(id=1)
        dto = TokenCDTO(
            access_token=access_token,
            refresh_token=token.refresh_token
        )
        await self.repository.update(obj=token, dto=dto)
