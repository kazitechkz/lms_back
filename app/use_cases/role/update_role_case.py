from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleCDTO, RoleRDTO
from app.adapters.repositories.role.role_repository import RoleRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateRoleCase(BaseUseCase[RoleRDTO]):
    def __init__(self, db: AsyncSession):
        self.role_repository = RoleRepository(db)

    async def execute(self, id: int, dto: RoleCDTO) -> RoleRDTO:
        obj = await self.validate(repository=self.role_repository, id=id, dto=dto)
        data = await self.role_repository.update(obj=obj, dto=dto)
        return RoleRDTO.from_orm(data)

    async def validate(self, repository: RoleRepository, id: int, dto: RoleCDTO):
        existed = await self.role_repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Роль не найдена")
        if await repository.get_first_with_filters(
            [repository.model.value == dto.value, repository.model.id != id]
        ):
            raise AppExceptionResponse.bad_request(
                "Роль с таким значением уже существует"
            )
        return existed
