from typing import Optional

from fastapi import File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.user.user_dto import UserRDTOWithRelated, UserCDTO
from app.adapters.repositories.role.role_repository import RoleRepository
from app.adapters.repositories.user.user_repository import UserRepository
from app.adapters.repositories.user_type.user_type_repository import UserTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.create_file_case import CreateFileCase


class UpdateUserCase(BaseUseCase[UserRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)
        self.role_repo = RoleRepository(db)
        self.user_type_repo = UserTypeRepository(db)
        self.file_use_case = CreateFileCase(db)

    async def execute(self, id: int,
                      dto: UserCDTO,
                      userDTO: UserRDTOWithRelated,
                      file: Optional[File] = None) -> UserRDTOWithRelated:
        obj = await self.validate(id=id, dto=dto, file=file, userDTO=userDTO)
        data = await self.repository.update(obj=obj, dto=dto, options=[
                joinedload(self.repository.model.user_type),
                joinedload(self.repository.model.role),
                joinedload(self.repository.model.file),
            ])
        return UserRDTOWithRelated.from_orm(data)

    async def validate(self, id: int, dto: UserCDTO, userDTO: UserRDTOWithRelated, file: Optional[File] = None):
        existed = await self.repository.get(id=id, options=[
                joinedload(self.repository.model.user_type),
                joinedload(self.repository.model.role),
                joinedload(self.repository.model.file),
            ])
        if existed is None:
            raise AppExceptionResponse.not_found(message="Пользователь не найдена")
        if await self.user_type_repo.get(id=dto.user_type_id) is None:
            raise AppExceptionResponse.not_found(message="Тип пользователя не найден")
        if await self.role_repo.get(id=dto.role_id) is None:
            raise AppExceptionResponse.not_found(message="Такой роли не существует")
        if file is not None:
            file = await self.file_use_case.execute(file=file, userDTO=userDTO, upload_path="avatars/")
            dto.file_id = file.id
        return existed
