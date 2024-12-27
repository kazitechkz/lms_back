from typing import Optional

from fastapi import File
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.user.user_dto import UserCDTO, UserRDTOWithRelated
from app.adapters.repositories.role.role_repository import RoleRepository
from app.adapters.repositories.user.user_repository import UserRepository
from app.adapters.repositories.user_type.user_type_repository import UserTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.create_file_case import CreateFileCase


class CreateUserCase(BaseUseCase[UserRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repo = UserRepository(db)
        self.role_repo = RoleRepository(db)
        self.user_type_repo = UserTypeRepository(db)
        self.file_use_case = CreateFileCase(db)

    async def execute(self, dto: UserCDTO, userDTO: UserRDTOWithRelated, file: Optional[File] = None):
        obj = await self.validate(dto=dto, userDTO=userDTO, file=file)
        data = await self.repo.create(obj=obj)
        return UserRDTOWithRelated.from_orm(data)

    async def validate(self, dto: UserCDTO, userDTO: UserRDTOWithRelated, file: Optional[File] = None):
        if await self.user_type_repo.get(id=dto.user_type_id):
            raise AppExceptionResponse.not_found(message="Тип пользователя не найден")
        if await self.role_repo.get(id=dto.role_id):
            raise AppExceptionResponse.not_found(message="Такой роли не существует")
        if file is not None:
            file = await self.file_use_case.execute(file=file, userDTO=userDTO, upload_path="avatars/")
            dto.file_id = file.id
        print(f"dto: {dto}")
        breakpoint()
        return self.repo.model(**dto.dict())
