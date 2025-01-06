from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.role_permission.role_permission_repository import RolePermissionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class DeleteRolePermissionCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = RolePermissionRepository(db)

    async def execute(self, id: int) -> bool:
        await self.validate(id=id)
        return await self.repository.delete(id=id)

    async def validate(self, id: int):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.bad_request(message="Право не найдено")
