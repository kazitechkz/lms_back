from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.pagination_dto import PaginationTests
from app.adapters.dto.test.test_dto import TestRDTO
from app.adapters.filters.test.test_filter import TestFilter
from app.adapters.repositories.test.test_repository import TestRepository
from app.use_cases.base_case import BaseUseCase


class AllTestsCase(BaseUseCase[PaginationTests]):
    def __init__(self, db: AsyncSession):
        self.repository = TestRepository(db)

    async def execute(self, params: TestFilter):
        tests = await self.repository.paginate(
            dto=TestRDTO,
            page=params.page,
            per_page=params.per_page,
            filters=params.apply()
        )
        return tests

    async def validate(self):
        pass
