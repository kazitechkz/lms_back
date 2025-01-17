import asyncio
import requests

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.token.token_dto import TokenRDTO, TokenCDTO
from app.adapters.repositories.token.token_repository import TokenRepository
from app.core.app_exception_response import AppExceptionResponse
from app.infrastructure.config import app_config
from app.use_cases.base_case import BaseUseCase


class CreateTokenCase(BaseUseCase[TokenRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = TokenRepository(db)

    async def execute(self, device_code: str):
        res = await self.validate(device_code=device_code)

        if res is False:
            return False
        else:
            return True

    async def validate(self, device_code: str):
        token = await self.repository.get(id=1)
        if token is None:
            data = {
                "access_token": "",
                "refresh_token": ""
            }
            token = await self.repository.create(obj=self.repository.model(**data))
        if not device_code:
            raise AppExceptionResponse.bad_request(message="device_code is required")
        tokens = await self.wait_for_authorization(
            client_id=app_config.google_client_id,
            client_secret=app_config.google_secret,
            device_code=device_code
        )
        if tokens.get('error'):
            return False
        dto = TokenCDTO(
            access_token=tokens.get('access_token'),
            refresh_token=tokens.get('refresh_token')
        )
        await self.repository.update(obj=token, dto=dto)

    async def wait_for_authorization(self, client_id, client_secret, device_code, interval=5.0):
        """
        Ожидание завершения авторизации пользователя.
        """
        token_url = "https://oauth2.googleapis.com/token"

        while True:
            # await asyncio.sleep(interval)
            token_payload = {
                "client_id": client_id,
                "client_secret": client_secret,
                "device_code": device_code,
                "grant_type": "urn:ietf:params:oauth:grant-type:device_code"
            }
            token_response = requests.post(token_url, data=token_payload)
            if token_response.status_code == 200:
                print("Пользователь успешно авторизовался.")
                return token_response.json()
            elif token_response.json().get("error") == "authorization_pending":
                print("Ожидание авторизации пользователя...")
                return token_response.json()
            else:
                raise AppExceptionResponse.bad_request(
                    message=f"Ошибка авторизации устройства: {token_response.status_code} - {token_response.text}"
                )
