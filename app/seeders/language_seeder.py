from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.language import LanguageModel
from app.infrastructure.db_constants import AppDbValueConstants, AppTableNames
from app.seeders.base_seeder import BaseSeeder


class LanguageSeeder(BaseSeeder):
    """Сидер для языков."""

    async def seed(self, session: AsyncSession):
        """Добавление базовых языков."""
        languages = self.get_data()
        await self.load_seeders(
            LanguageModel, session, AppTableNames.LanguageTableName, languages
        )

    def get_dev_data(self):
        """Языки для разработки."""
        return [
            LanguageModel(
                title="Русский язык", value=AppDbValueConstants.RUSSIAN_VALUE
            ),
            LanguageModel(title="Қазақ тілі", value=AppDbValueConstants.KAZAKH_VALUE),
            LanguageModel(title="English", value=AppDbValueConstants.ENGLISH_VALUE),
        ]

    def get_prod_data(self):
        return [
            LanguageModel(
                title="Русский язык", value=AppDbValueConstants.RUSSIAN_VALUE
            ),
            LanguageModel(title="Қазақ тілі", value=AppDbValueConstants.KAZAKH_VALUE),
            LanguageModel(title="English", value=AppDbValueConstants.ENGLISH_VALUE),
        ]
