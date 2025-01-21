from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.organization_type.organization_type_dto import OrganizationTypeCDTO, OrganizationTypeRDTO
from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.dto.test_type.tag_type_dto import TestTypeRDTO, TestTypeCDTO
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.organizaiton_type.all_organization_types_case import AllOrganizationTypesCase
from app.use_cases.organizaiton_type.create_organization_type_case import CreateOrganizationTypeCase
from app.use_cases.organizaiton_type.delete_organization_type_case import DeleteOrganizationTypeCase
from app.use_cases.organizaiton_type.get_organization_type_by_value_case import GetOrganizationTypeByValueCase
from app.use_cases.organizaiton_type.get_organization_type_case import GetOrganizationTypeCase
from app.use_cases.organizaiton_type.update_organization_type_case import UpdateOrganizationTypeCase
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase
from app.use_cases.test_type.all_test_types_case import AllTestTypesCase
from app.use_cases.test_type.create_test_type_case import CreateTestTypeCase
from app.use_cases.test_type.delete_test_type_case import DeleteTestTypeCase
from app.use_cases.test_type.get_test_type_by_value_case import GetTestTypeByValueCase
from app.use_cases.test_type.get_test_type_case import GetTestTypeCase
from app.use_cases.test_type.update_test_type_case import UpdateTestTypeCase


class OrganizationTypeApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[OrganizationTypeRDTO],
            summary="Список типов организации",
            description="Получение списка типов организаций",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=OrganizationTypeRDTO,
            summary="Получить тип организации по уникальному ID",
            description="Получение типов организаций по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=OrganizationTypeRDTO,
            summary="Получить тип организации по уникальному значению",
            description="Получение типов организаций по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=OrganizationTypeRDTO,
            summary="Создать тип организации",
            description="Создание типов организаций",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=OrganizationTypeRDTO,
            summary="Обновить тип организации по уникальному ID",
            description="Обновление типов организаций по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить тип организации по уникальному ID",
            description="Удаление типов организаций по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))):
        use_case = AllOrganizationTypesCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))):
        use_case = GetOrganizationTypeCase(db)
        return await use_case.execute(org_type_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))
    ):
        use_case = GetOrganizationTypeByValueCase(db)
        return await use_case.execute(org_type_value=value)

    async def create(self, dto: OrganizationTypeCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_ROLE_VALUE))):
        use_case = CreateOrganizationTypeCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: OrganizationTypeCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_ROLE_VALUE))
    ):
        use_case = UpdateOrganizationTypeCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_ROLE_VALUE))
    ):
        use_case = DeleteOrganizationTypeCase(db)
        return await use_case.execute(id=id)
