from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.permission.permission_dto import PermissionRDTO
from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.repositories.permission.permission_repository import PermissionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetPermissionCase(BaseUseCase[PermissionRDTO]):
    """Use Case для получения роли по ID."""

    def __init__(self, db: AsyncSession):
        self.permission_repository = PermissionRepository(db)

    async def execute(self, permission_id: int) -> PermissionRDTO:
        """Получение роли по ID."""

        return PermissionRDTO.from_orm(permission)

    async def validate(self, repo: PermissionRepository, id: int):
        permission = await repo.get(id)
        if not permission:
            raise AppExceptionResponse.not_found("Право не найдено")
