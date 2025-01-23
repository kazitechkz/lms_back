from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.organization.organization_dto import OrganizationRDTOWithRelated, OrganizationCDTO, \
    OrganizationRDTO
from app.adapters.dto.pagination_dto import PaginationOrganizations
from app.adapters.filters.organization.organization_filter import OrganizationFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.organization.all_organizations_case import AllOrganizationsCase
from app.use_cases.organization.create_organization_case import CreateOrganizationCase
from app.use_cases.organization.delete_organization_case import DeleteOrganizationCase
from app.use_cases.organization.get_organization_by_bin_case import GetOrganizationByValueCase
from app.use_cases.organization.get_organization_case import GetOrganizationCase
from app.use_cases.organization.update_organization_case import UpdateOrganizationCase


class OrganizationApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=PaginationOrganizations,
            summary="Список организаций",
            description="Получение списка организаций",
        )(self.get_all)
        self.router.get(
            "/get-without-paginate",
            response_model=list[OrganizationRDTO],
            summary="Список организаций",
            description="Получение списка организаций",
        )(self.get_all_without_paginate)
        self.router.get(
            "/get/{id}",
            response_model=OrganizationRDTOWithRelated,
            summary="Получить организацию по уникальному ID",
            description="Получение организации по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-bin/{value}",
            response_model=OrganizationRDTOWithRelated,
            summary="Получить организацию по БИН значению",
            description="Получение организации по БИН значению",
        )(self.get_by_bin)
        self.router.post(
            "/create",
            response_model=OrganizationRDTOWithRelated,
            summary="Создать организацию",
            description="Создание организации",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=OrganizationRDTOWithRelated,
            summary="Обновить организацию по уникальному ID",
            description="Обновление организации по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалите организацию по уникальному ID",
            description="Удаление организации по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      params: OrganizationFilter = Depends(),
                      user=Depends(permission_dependency(PermissionConstants.READ_ORGANIZATION_VALUE))):
        use_case = AllOrganizationsCase(db)
        return await use_case.execute(params=params)

    async def get_all_without_paginate(self, db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_ORGANIZATION_VALUE))):
        use_case = AllOrganizationsCase(db)
        return await use_case.get_all_without_paginate()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_ORGANIZATION_VALUE))):
        use_case = GetOrganizationCase(db)
        return await use_case.execute(organization_id=id)

    async def get_by_bin(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.READ_ORGANIZATION_VALUE))
    ):
        use_case = GetOrganizationByValueCase(db)
        return await use_case.execute(bin=value)

    async def create(self, dto: OrganizationCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_ORGANIZATION_VALUE))):
        use_case = CreateOrganizationCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: OrganizationCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_ORGANIZATION_VALUE))
    ):
        use_case = UpdateOrganizationCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_ORGANIZATION_VALUE))
    ):
        use_case = DeleteOrganizationCase(db)
        return await use_case.execute(id=id)
