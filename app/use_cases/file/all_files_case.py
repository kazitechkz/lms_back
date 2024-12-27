from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleRDTO
from app.adapters.repositories.role.role_repository import RoleRepository
from app.use_cases.base_case import BaseUseCase


class AllRolesCase(BaseUseCase[List[RoleRDTO]]):
    def __init__(self, db: AsyncSession):
        self.role_repository = RoleRepository(db)

    async def execute(self) -> List[RoleRDTO]:
        roles = await self.role_repository.get_all()
        return [RoleRDTO.from_orm(role) for role in roles]

    async def validate(self):
        pass
