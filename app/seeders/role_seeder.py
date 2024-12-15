from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.role import RoleModel
from app.infrastructure.db_constants import AppDbValueConstants, AppTableNames
from app.seeders.base_seeder import BaseSeeder


class RoleSeeder(BaseSeeder):
    async def seed(self, session: AsyncSession):
        roles = self.get_data()
        await self.load_seeders(RoleModel, session, AppTableNames.RoleTableName, roles)

    def get_dev_data(self):
        return [
            RoleModel(
                title_ru="Администратор",
                title_kk="Администратор",
                title_en="Administrator",
                value=AppDbValueConstants.ADMINISTRATOR_VALUE,
                can_register=False,
                is_admin=True,
            ),
            RoleModel(
                title_ru="Модератор",
                title_kk="Модератор",
                title_en="Moderator",
                value=AppDbValueConstants.MODERATOR_VALUE,
                can_register=False,
                is_admin=True,
            ),
            RoleModel(
                title_ru="Руководство компании",
                title_kk="Компания басшылығы",
                title_en="Company Lead",
                value=AppDbValueConstants.COMPANY_LEAD_VALUE,
                can_register=True,
                is_admin=False,
            ),
            RoleModel(
                title_ru="Менеджер компании",
                title_kk="Компания менеджері",
                title_en="Company Manager",
                value=AppDbValueConstants.COMPANY_MANAGER_VALUE,
                can_register=False,
                is_admin=False,
            ),
            RoleModel(
                title_ru="Сотрудник",
                title_kk="Қызметкер",
                title_en="Employee",
                value=AppDbValueConstants.EMPLOYEE_VALUE,
                can_register=False,
                is_admin=False,
            ),
        ]

    def get_prod_data(self):
        return [
            RoleModel(
                title_ru="Администратор",
                title_kk="Администратор",
                title_en="Administrator",
                value=AppDbValueConstants.ADMINISTRATOR_VALUE,
                can_register=False,
                is_admin=True,
            ),
            RoleModel(
                title_ru="Модератор",
                title_kk="Модератор",
                title_en="Moderator",
                value=AppDbValueConstants.MODERATOR_VALUE,
                can_register=False,
                is_admin=True,
            ),
            RoleModel(
                title_ru="Руководство компании",
                title_kk="Компания басшылығы",
                title_en="Company Lead",
                value=AppDbValueConstants.COMPANY_LEAD_VALUE,
                can_register=True,
                is_admin=False,
            ),
            RoleModel(
                title_ru="Менеджер компании",
                title_kk="Компания менеджері",
                title_en="Company Manager",
                value=AppDbValueConstants.COMPANY_MANAGER_VALUE,
                can_register=False,
                is_admin=False,
            ),
            RoleModel(
                title_ru="Сотрудник",
                title_kk="Қызметкер",
                title_en="Employee",
                value=AppDbValueConstants.EMPLOYEE_VALUE,
                can_register=False,
                is_admin=False,
            ),
        ]
