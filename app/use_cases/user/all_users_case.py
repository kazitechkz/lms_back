from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.pagination_dto import PaginationUsers
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.filters.users.user_filter import UserFilter
from app.adapters.repositories.user.user_repository import UserRepository
from app.use_cases.base_case import BaseUseCase


class AllUsersCase(BaseUseCase[PaginationUsers]):
    def __init__(self, db: AsyncSession):
        self.repository = UserRepository(db)

    async def execute(self, params: UserFilter):
        users = await self.repository.paginate(
            dto=UserRDTOWithRelated,
            page=params.page,
            per_page=params.per_page,
            options=[
                joinedload(self.repository.model.user_type),
                joinedload(self.repository.model.role),
                joinedload(self.repository.model.file),
            ]
        )
        return users

    async def validate(self):
        pass
