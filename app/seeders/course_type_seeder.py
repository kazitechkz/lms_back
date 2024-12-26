from sqlalchemy.ext.asyncio import AsyncSession

from app.entities.course_type import CourseTypeModel
from app.infrastructure.db_constants import AppDbValueConstants, AppTableNames
from app.seeders.base_seeder import BaseSeeder


class CourseTypeSeeder(BaseSeeder):

    async def seed(self, session: AsyncSession):
        course_types = self.get_data()
        await self.load_seeders(
            CourseTypeModel, session, AppTableNames.CourseTypeTableName, course_types
        )

    def get_dev_data(self):
        return [
            CourseTypeModel(
                title_ru="Открытые платные",
                title_kk="Ашық ақылы",
                title_en="Paid",
                value=AppDbValueConstants.PAID_VALUE,
            ),
            CourseTypeModel(
                title_ru="Приватные",
                title_kk="Жабық",
                title_en="Private",
                value=AppDbValueConstants.PRIVATE_VALUE,
            ),
            CourseTypeModel(
                title_ru="Бесплатные",
                title_kk="Тегін",
                title_en="Free",
                value=AppDbValueConstants.FREE_VALUE,
            )
        ]

    def get_prod_data(self):
        return [
            CourseTypeModel(
                title_ru="Открытые платные",
                title_kk="Ашық ақылы",
                title_en="Paid",
                value=AppDbValueConstants.PAID_VALUE,
            ),
            CourseTypeModel(
                title_ru="Приватные",
                title_kk="Жабық",
                title_en="Private",
                value=AppDbValueConstants.PRIVATE_VALUE,
            ),
            CourseTypeModel(
                title_ru="Бесплатные",
                title_kk="Тегін",
                title_en="Free",
                value=AppDbValueConstants.FREE_VALUE,
            )
        ]
