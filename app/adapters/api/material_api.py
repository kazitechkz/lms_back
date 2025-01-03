from typing import Optional

from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.material.material_dto import MaterialRDTO, MaterialCDTO, MaterialRDTOWithRelated
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.material.create_material_case import CreateMaterialCase
from app.use_cases.material.delete_material_case import DeleteMaterialCase
from app.use_cases.material.get_material_case import GetMaterialCase
from app.use_cases.material.update_material_case import UpdateMaterialCase


class MaterialApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/get/{id}",
            response_model=MaterialRDTOWithRelated,
            summary="Получить материал по уникальному ID",
            description="Получение материала по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=MaterialRDTO,
            summary="Создать материал",
            description="Создание материала",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=MaterialRDTO,
            summary="Обновить материал",
            description="Обновление материала",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить материал по уникальному ID",
            description="Удаление материала по уникальному идентификатору",
        )(self.delete)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_MATERIAL_VALUE))):
        use_case = GetMaterialCase(db)
        return await use_case.execute(material_id=id)

    async def create(self, dto: MaterialCDTO = Depends(),
                     file: UploadFile = File(description="Файл для загрузки"),
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_MATERIAL_VALUE))):
        use_case = CreateMaterialCase(db)
        return await use_case.execute(dto=dto, userDTO=user, file=file)

    async def update(self, id: PathConstants.IDPath, dto: MaterialCDTO = Depends(),
                     file: Optional[UploadFile] = File(default=None, description="Файл для загрузки"),
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.UPDATE_MATERIAL_VALUE))):
        use_case = UpdateMaterialCase(db)
        return await use_case.execute(id=id, dto=dto, userDTO=user, file=file)

    async def delete(
            self,
            id: PathConstants.IDPath,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_MATERIAL_VALUE))
    ):
        use_case = DeleteMaterialCase(db)
        return await use_case.execute(id=id)
