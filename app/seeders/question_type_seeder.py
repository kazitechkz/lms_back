from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.question_type import QuestionTypeModel
from app.infrastructure.db_constants import AppDbValueConstants, AppTableNames
from app.seeders.base_seeder import BaseSeeder


class QuestionTypeSeeder(BaseSeeder):

    async def seed(self, session: AsyncSession):
        question_type = self.get_data()
        await self.load_seeders(
            QuestionTypeModel, session, AppTableNames.QuestionTypeTableName, question_type
        )

    def get_dev_data(self):
        return [
            QuestionTypeModel(
                title_ru="С одним выбором",
                title_kk="Бір жауапты",
                title_en="Single choice",
                value=AppDbValueConstants.SINGLE_CHOICE_VALUE
            ),
            QuestionTypeModel(
                title_ru="Много выборов",
                title_kk="Көп жауапты",
                title_en="Multiple choices",
                value=AppDbValueConstants.MULTIPLE_CHOICE_VALUE
            )
        ]

    def get_prod_data(self):
        return self.get_dev_data()
