from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.repositories.role.role_repository import RoleRepository
from app.use_cases.base_case import BaseUseCase


class GetRoleCase(BaseUseCase[RoleRDTO]):
    """Use Case для получения роли по ID."""

    def __init__(self, db: AsyncSession):
        self.role_repository = RoleRepository(db)

    async def execute(self, role_id: int) -> RoleRDTO:
        """Получение роли по ID."""
        role = await self.role_repository.get(role_id)
        if not role:
            raise ValueError("Роль не найдена")
        return RoleRDTO.from_orm(role)
