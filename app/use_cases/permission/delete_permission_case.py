from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.permission.permission_repository import PermissionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class DeletePermissionCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.permission_repository = PermissionRepository(db)

    async def execute(self, id: int) -> bool:
        await self.validate(repository=self.permission_repository, id=id)
        return await self.permission_repository.delete(id=id)

    async def validate(self, repository: PermissionRepository, id: int):
        existed = await self.permission_repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Право не найдено")
