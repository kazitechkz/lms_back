from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from app.core.app_exception_response import AppExceptionResponse
from app.infrastructure.config import app_config

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Функция для создания токена доступа
def create_access_token(data: int):
    to_encode = {"sub": str(data), "type": "access"}
    expire = datetime.now() + timedelta(minutes=app_config.access_token_expire_minutes)
    to_encode.update({"exp": expire.timestamp()})
    encoded_jwt = jwt.encode(
        to_encode, app_config.secret_key, algorithm=app_config.algorithm
    )
    return encoded_jwt


# Функция для создания refresh токена
def create_refresh_token(data: int):
    to_encode = {
        "sub": str(data),
        "type": "refresh",
    }  # Указываем тип токена как "refresh"
    expire = datetime.now() + timedelta(days=app_config.refresh_token_expire_days)
    to_encode.update({"exp": expire.timestamp()})
    encoded_jwt = jwt.encode(
        to_encode, app_config.secret_key, algorithm=app_config.algorithm
    )
    return encoded_jwt

def verify_token(token_type: str, token: str = Depends(oauth2_scheme)) -> dict:
    try:
        decoded_data = jwt.decode(
            token, app_config.secret_key, algorithms=[app_config.algorithm]
        )
        if decoded_data.get("type") != token_type:
            raise AppExceptionResponse.forbidden(
                message=f"Недопустимый токен для {token_type}",
            )
        return decoded_data
    except jwt.JWTError as jwtError:
         raise AppExceptionResponse.unauthorized(
                message=f"Не удалось проверить токен: {jwtError!s}",
            )

def check_token_expiry(decoded_token: dict):
    expire = decoded_token.get("exp")
    if not expire or int(expire) < datetime.now().timestamp():
        raise AppExceptionResponse.unauthorized(
            message=f"Срок действия токена истёк",
        )
