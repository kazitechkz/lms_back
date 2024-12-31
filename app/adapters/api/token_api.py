from fastapi import APIRouter, Depends, Form
from pydantic import Field
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database import get_db
from app.use_cases.token.create_token_case import CreateTokenCase


class TokenApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.post(
            "/check_token",
            response_model=bool,
            summary="Проверка ютуб токена",
            description="Получение авторизационного токена с ютуба",
        )(self.wait_for_authorization)

    async def wait_for_authorization(self, device_code: str = Form(description="Device code"),
                                     db: AsyncSession = Depends(get_db)):
        use_case = CreateTokenCase(db)
        return await use_case.execute(device_code=device_code)
