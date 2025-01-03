from fastapi import File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.material.material_dto import MaterialCDTO, MaterialRDTO
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.repositories.material.material_repository import MaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.create_file_case import CreateFileCase


class CreateMaterialCase(BaseUseCase[MaterialRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = MaterialRepository(db)
        self.file_use_case = CreateFileCase(db)

    async def execute(self, dto: MaterialCDTO,
                      userDTO: UserRDTOWithRelated, file: File, upload_path: str = "materials/"):
        # Проверяем и валидируем входные данные
        obj = await self.validate(dto=dto, file=file, userDTO=userDTO, upload_path=upload_path)
        data = await self.repository.create(obj=obj, options=[joinedload(self.repository.model.file)])
        return MaterialRDTO.from_orm(data)

    async def validate(self, dto: MaterialCDTO, userDTO: UserRDTOWithRelated, file: File,
                       upload_path: str = "materials/"):
        if not file:
            raise AppExceptionResponse.bad_request("Файл не загружен")
        file_obj = await self.file_use_case.execute(file=file, userDTO=userDTO, upload_path=upload_path)
        dto.file_id = file_obj.id
        return self.repository.model(**dto.dict())
