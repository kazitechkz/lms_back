from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.user_type import UserTypeModel
from app.infrastructure.db_constants import AppDbValueConstants, AppTableNames
from app.seeders.base_seeder import BaseSeeder


class UserTypeSeeder(BaseSeeder):
    """Сидер для типов пользователей."""

    async def seed(self, session: AsyncSession):
        """Добавление базовых типов пользователей."""
        user_types = self.get_data()
        await self.load_seeders(
            UserTypeModel, session, AppTableNames.UserTypeTableName, user_types
        )

    def get_dev_data(self):
        """Типы пользователей для разработки."""
        return [
            UserTypeModel(
                title_ru="Физическое лицо",
                title_kk="Жеке тұлға",
                title_en="Individual",
                value=AppDbValueConstants.INDIVIDUAL_VALUE,
            ),
            UserTypeModel(
                title_ru="Юридическое лицо",
                title_kk="Заңды тұлға",
                title_en="Legal entity",
                value=AppDbValueConstants.LEGAL_VALUE,
            ),
        ]

    def get_prod_data(self):
        """Типы пользователей для продакшена."""
        return [
            UserTypeModel(
                title_ru="Физическое лицо",
                title_kk="Жеке тұлға",
                title_en="Individual",
                value=AppDbValueConstants.INDIVIDUAL_VALUE,
            ),
            UserTypeModel(
                title_ru="Юридическое лицо",
                title_kk="Заңды тұлға",
                title_en="Legal entity",
                value=AppDbValueConstants.LEGAL_VALUE,
            ),
        ]  # Используем те же данные
