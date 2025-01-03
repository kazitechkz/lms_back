from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.material.material_dto import MaterialRDTOWithRelated
from app.adapters.repositories.material.material_repository import MaterialRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class GetMaterialCase(BaseUseCase[MaterialRDTOWithRelated]):

    def __init__(self, db: AsyncSession):
        self.repository = MaterialRepository(db)

    async def execute(self, material_id: int) -> MaterialRDTOWithRelated:
        material = await self.validate(material_id=material_id)
        return MaterialRDTOWithRelated.from_orm(material)

    async def validate(self, material_id: int):
        material = await self.repository.get(material_id, options=[
            joinedload(self.repository.model.file)
        ])
        if not material:
            raise AppExceptionResponse.not_found("Материал не найден")
        return material
