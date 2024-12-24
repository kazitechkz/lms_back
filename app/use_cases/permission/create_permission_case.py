from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.permission.permission_dto import PermissionRDTO, PermissionCDTO
from app.adapters.repositories.permission.permission_repository import PermissionRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreatePermissionCase(BaseUseCase[PermissionRDTO]):
    def __init__(self, db: AsyncSession):
        self.permission_repository = PermissionRepository(db)

    async def execute(self, dto: PermissionCDTO) -> PermissionRDTO:
        obj = await self.validate(repository=self.permission_repository, dto=dto)
        data = await self.permission_repository.create(obj=obj)
        return PermissionRDTO.from_orm(data)

    async def validate(self, repository: PermissionRepository, dto: PermissionCDTO):
        if await repository.get_first_with_filters(
            [repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Право с таким значением уже существует"
            )
        return self.permission_repository.model(**dto.dict())
