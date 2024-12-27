from fastapi import HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette import status


class AuthBearer(HTTPBearer):
    async def __call__(self, request: Request) -> str | None:
        try:
            credentials: HTTPAuthorizationCredentials = await super().__call__(request)
            return credentials.credentials  # Возвращаем Bearer токен
        except HTTPException as ex:
            if ex.status_code == status.HTTP_403_FORBIDDEN:
                return None  # Если токена нет, возвращаем None
            raise
