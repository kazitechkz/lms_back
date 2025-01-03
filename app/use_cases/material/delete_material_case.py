from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.repositories.material.material_repository import MaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.delete_file_case import DeleteFileCase


class DeleteMaterialCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = MaterialRepository(db)
        self.delete_file = DeleteFileCase(db)

    async def execute(self, id: int) -> bool:
        await self.validate(id=id)
        data = await self.repository.delete(id=id)
        return data

    async def validate(self, id: int):
        existed = await self.repository.get(id=id, options=[
            joinedload(self.repository.model.file)
        ])
        if existed is None:
            raise AppExceptionResponse.not_found(message="Материал не найден")
        if existed.file is not None:
            await self.delete_file.execute(existed.file.file_path)
