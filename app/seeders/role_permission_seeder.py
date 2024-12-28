from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.entities import PermissionModel, RolePermissionModel
from app.infrastructure.db_constants import AppTableNames
from app.seeders.base_seeder import BaseSeeder


class RolePermissionSeeder:

    async def seed(self, session: AsyncSession):
        permissions = await session.execute(select(PermissionModel))
        permissions = permissions.scalars().all()

        role_permissions = []
        for permission in permissions:
            role_permissions.append({
                "role_id": 1,
                "permission_id": permission.id,
            })

        await self.load_seeders(
            RolePermissionModel, session, AppTableNames.RolePermissionTableName, role_permissions
        )

    async def load_seeders(self, model, session, table_name, data):
        """
        Метод для массового добавления данных в таблицу.
        """
        existing_data = await session.execute(select(model))
        existing_data = existing_data.scalars().all()

        new_entries = []
        for item in data:
            # Создаём экземпляр модели вместо словаря
            if not any(
                    existing.role_id == item["role_id"] and
                    existing.permission_id == item["permission_id"]
                    for existing in existing_data
            ):
                new_entries.append(model(**item))  # Создаём экземпляр модели

        session.add_all(new_entries)
        await session.commit()
