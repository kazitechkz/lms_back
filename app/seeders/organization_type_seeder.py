from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.organization_type import OrganizationTypeModel
from app.infrastructure.db_constants import AppDbValueConstants, AppTableNames
from app.seeders.base_seeder import BaseSeeder


class OrganizationTypeSeeder(BaseSeeder):
    """Сидер для типов организаций."""

    async def seed(self, session: AsyncSession):
        """Добавление базовых типов организаций."""
        organization_types = self.get_data()
        await self.load_seeders(
            OrganizationTypeModel,
            session,
            AppTableNames.OrganizationTypeTableName,
            organization_types,
        )

    def get_dev_data(self):
        """Типы организаций для разработки."""
        return [
            OrganizationTypeModel(
                title_ru="Товарищество с ограниченной ответственностью",
                title_kk="Жауапкершілігі шектеулі серіктестік",
                title_en="Limited Liability Partnership",
                value=AppDbValueConstants.LLP_VALUE,
            ),
            OrganizationTypeModel(
                title_ru="Индивидуальный предприниматель",
                title_kk="Жеке кәсіпкер",
                title_en="Individual Entrepreneur",
                value=AppDbValueConstants.IE_VALUE,
            ),
            OrganizationTypeModel(
                title_ru="Акционерное общество",
                title_kk="Акционерлік қоғам",
                title_en="Joint Stock Company",
                value=AppDbValueConstants.JCS_VALUE,
            ),
            OrganizationTypeModel(
                title_ru="Государственная корпорация",
                title_kk="Мемлекеттік корпорация",
                title_en="State Corporation",
                value=AppDbValueConstants.SC_VALUE,
            ),
            OrganizationTypeModel(
                title_ru="Крестьянское хозяйство",
                title_kk="Шаруа қожалығы",
                title_en="Farm Enterprise",
                value=AppDbValueConstants.FE_VALUE,
            ),
            OrganizationTypeModel(
                title_ru="Производственный кооператив",
                title_kk="Өндірістік кооператив",
                title_en="Production Cooperative",
                value=AppDbValueConstants.PC_VALUE,
            ),
            OrganizationTypeModel(
                title_ru="Некоммерческое Акционерное общество",
                title_kk="Коммерциялық емес акционерлік қоғам",
                title_en="Non-Profit Joint Stock Company",
                value=AppDbValueConstants.NON_JCS_VALUE,
            ),
        ]

    def get_prod_data(self):
        """Типы организаций для продакшена."""
        return self.get_dev_data()  # Используем те же данные
