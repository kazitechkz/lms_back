from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.auth.auth_dto import AuthCDTO
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.core.auth_core import get_current_user
from app.infrastructure.database import get_db
from app.use_cases.auth.auth_login_case import AuthLoginUseCase


class AuthApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.post("/login")(self.login)
        self.router.get("/me")(self.me)

    async def login(self,
                     dto: AuthCDTO,
                     db: AsyncSession = Depends(get_db)):
        use_case = AuthLoginUseCase(db)
        return await use_case.execute(dto=dto)

    async def me(self, db: AsyncSession = Depends(get_db), user: UserRDTOWithRelated = Depends(get_current_user)):
        return user
