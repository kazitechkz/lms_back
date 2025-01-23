from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.adapters.dto.pagination_dto import PaginationTests
from app.adapters.dto.test.test_dto import TestRDTO, TestRDTOWithRelated
from app.adapters.filters.test.test_filter import TestFilter
from app.adapters.repositories.test.test_repository import TestRepository
from app.use_cases.base_case import BaseUseCase


class AllTestsCase(BaseUseCase[PaginationTests]):
    def __init__(self, db: AsyncSession):
        self.repository = TestRepository(db)

    async def execute(self, params: TestFilter):
        tests = await self.repository.paginate(
            dto=TestRDTOWithRelated,
            page=params.page,
            per_page=params.per_page,
            filters=params.apply(),
            options=[
                selectinload(self.repository.model.type)
            ]
        )
        return tests

    async def validate(self):
        pass
