from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from starlette import status

from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.core.app_exception_response import AppExceptionResponse
from app.entities import UserModel
from app.infrastructure.config import app_config
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import AppDbValueConstants

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


async def get_current_user(
        token: str = Depends(verify_token), db: AsyncSession = Depends(get_db)
) -> UserRDTOWithRelated:
    # Проверка истечения срока действия токена
    expire = token.get("exp")
    if not expire or int(expire) < datetime.now().timestamp():
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Срок действия токена истек",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Получение идентификатора пользователя
    user_id = token.get("sub")
    if not user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Пользователь не найден {user_id!s}",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Запрос к базе данных для получения пользователя
    query = (
        select(UserModel)
        .options(
            selectinload(UserModel.role),
            selectinload(UserModel.user_type),
            selectinload(UserModel.file),
        )
        .filter(UserModel.id == int(user_id))
    )

    result = await db.execute(query)
    user = result.scalars().first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Пользователь не найден",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Преобразование ORM-модели в DTO
    return UserRDTOWithRelated.from_orm(user)


def check_admin(current_user: UserRDTOWithRelated = Depends(get_current_user)):
    if current_user.role.value != AppDbValueConstants.ADMINISTRATOR_VALUE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Отказано в доступе",
        )
    return current_user


def check_moderator(current_user: UserRDTOWithRelated = Depends(get_current_user)):
    if current_user.role.value != AppDbValueConstants.MODERATOR_VALUE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Отказано в доступе",
        )
    return current_user


def check_company_lead(current_user: UserRDTOWithRelated = Depends(get_current_user)):
    if current_user.role.value != AppDbValueConstants.COMPANY_LEAD_VALUE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Отказано в доступе",
        )
    return current_user


def check_company_manager(current_user: UserRDTOWithRelated = Depends(get_current_user)):
    if current_user.role.value != AppDbValueConstants.COMPANY_MANAGER_VALUE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Отказано в доступе",
        )
    return current_user


def check_employee(current_user: UserRDTOWithRelated = Depends(get_current_user)):
    if current_user.role.value != AppDbValueConstants.EMPLOYEE_VALUE:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Отказано в доступе",
        )
    return current_user
