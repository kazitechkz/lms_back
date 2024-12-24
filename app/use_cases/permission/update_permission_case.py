from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.permission.permission_dto import PermissionRDTO, PermissionCDTO
from app.adapters.repositories.permission.permission_repository import PermissionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdatePermissionCase(BaseUseCase[PermissionRDTO]):
    def __init__(self, db: AsyncSession):
        self.permission_repository = PermissionRepository(db)

    async def execute(self, id: int, dto: PermissionCDTO) -> PermissionRDTO:
        obj = await self.validate(repository=self.permission_repository, id=id, dto=dto)
        data = await self.permission_repository.update(obj=obj, dto=dto)
        return PermissionRDTO.from_orm(data)

    async def validate(self, repository: PermissionRepository, id: int, dto: PermissionCDTO):
        existed = await self.permission_repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Право не найдено")
        if await repository.get_first_with_filters(
            [repository.model.value == dto.value, repository.model.id != id]
        ):
            raise AppExceptionResponse.bad_request(
                "Право с таким значением уже существует"
            )
        return existed
