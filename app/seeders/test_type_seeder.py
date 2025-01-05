from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.question_type import QuestionTypeModel
from app.entities.test import TestTypeModel
from app.infrastructure.db_constants import AppDbValueConstants, AppTableNames
from app.seeders.base_seeder import BaseSeeder


class TestTypeSeeder(BaseSeeder):

    async def seed(self, session: AsyncSession):
        test_type = self.get_data()
        await self.load_seeders(
            TestTypeModel, session, AppTableNames.TestTypeTableName, test_type
        )

    def get_dev_data(self):
        return [
            TestTypeModel(
                title_ru="Тест",
                title_kk="Тест",
                title_en="Test",
                value=AppDbValueConstants.TEST_VALUE
            ),
            TestTypeModel(
                title_ru="Экзамен",
                title_kk="Емтихан",
                title_en="Examen",
                value=AppDbValueConstants.EXAM_VALUE
            )
        ]

    def get_prod_data(self):
        return self.get_dev_data()
