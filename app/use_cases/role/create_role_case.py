from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.role.role_dto import RoleCDTO, RoleRDTO
from app.adapters.repositories.role.role_repository import RoleRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateRoleCase(BaseUseCase[RoleRDTO]):
    def __init__(self, db: AsyncSession):
        self.role_repository = RoleRepository(db)

    async def execute(self, dto: RoleCDTO) -> RoleRDTO:
        obj = await self.validate(repository=self.role_repository, dto=dto)
        data = await self.role_repository.create(obj=obj)
        return RoleRDTO.from_orm(data)

    async def validate(self, repository: RoleRepository, dto: RoleCDTO):
        if await repository.get_first_with_filters(
            [repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Роль с таким значением уже существует"
            )
        return repository.model(**dto.dict())
