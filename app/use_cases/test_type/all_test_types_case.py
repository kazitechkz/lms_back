from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.test_type.tag_type_dto import TestTypeRDTO
from app.adapters.repositories.test_type.test_type_repository import TestTypeRepository
from app.use_cases.base_case import BaseUseCase


class AllTestTypesCase(BaseUseCase[List[TestTypeRDTO]]):
    def __init__(self, db: AsyncSession):
        self.repository = TestTypeRepository(db)

    async def execute(self) -> List[TestTypeRDTO]:
        test_types = await self.repository.get_all()
        return [TestTypeRDTO.from_orm(test_type) for test_type in test_types]

    async def validate(self):
        pass
