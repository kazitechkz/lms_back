from typing import Optional

from fastapi import File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.material.material_dto import MaterialRDTO, MaterialCDTO
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.repositories.material.material_repository import MaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.entities.material import MaterialModel
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.create_file_case import CreateFileCase
from app.use_cases.file.delete_file_case import DeleteFileCase


class UpdateMaterialCase(BaseUseCase[MaterialRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = MaterialRepository(db)
        self.create_file = CreateFileCase(db)
        self.delete_file = DeleteFileCase(db)

    async def execute(self, id: int, dto: MaterialCDTO,
                      userDTO: UserRDTOWithRelated, file: Optional[File] = None) -> MaterialRDTO:
        obj = await self.validate(id=id, dto=dto, file=file, userDTO=userDTO)
        data = await self.repository.update(obj=obj, dto=dto)
        return MaterialRDTO.from_orm(data)

    async def validate(self, id: int, dto: MaterialCDTO,
                       userDTO: UserRDTOWithRelated, file: Optional[File] = None):
        existed = await self.repository.get(id=id, options=[joinedload(self.repository.model.file)])
        if existed is None:
            raise AppExceptionResponse.not_found(message="Материал не найден")
        if file:
            if existed.file and existed.file.file_path:
                await self.delete_file.execute(existed.file.file_path)
            new_file = await self.create_file.execute(file=file, userDTO=userDTO, upload_path="materials/")
            dto.file_id = new_file.id
        else:
            dto.file_id = existed.file_id

        return existed
