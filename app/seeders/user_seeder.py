from sqlalchemy.ext.asyncio import AsyncSession

from app.entities import UserModel
from app.entities.role import RoleModel
from app.infrastructure.db_constants import AppDbValueConstants, AppTableNames
from app.seeders.base_seeder import BaseSeeder


class UserSeeder(BaseSeeder):
    async def seed(self, session: AsyncSession):
        users = self.get_data()
        await self.load_seeders(UserModel, session, AppTableNames.UserTableName, users)

    def get_dev_data(self):
        return [
            UserModel(
                name="Admin",
                email="admin@gmail.com",
                password_hash="$2b$12$zhSpWTELxX8/N274Gy4wkOetqv02re2AYEv2LiXmGn4V4wCme6Hqe",
                phone="87474119784",
                position="...",
                is_active=True,
                role_id=1,
                user_type_id=1
            ),
            UserModel(
                name="Moder",
                email="moder@gmail.com",
                password_hash="$2b$12$zhSpWTELxX8/N274Gy4wkOetqv02re2AYEv2LiXmGn4V4wCme6Hqe",
                phone="87074119784",
                position="...",
                is_active=True,
                role_id=2,
                user_type_id=1
            ),
        ]

    def get_prod_data(self):
        return self.get_dev_data()
