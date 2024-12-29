from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.course_tag.course_tag_repository import CourseTagRepository
from app.use_cases.base_case import BaseUseCase


class DeleteCourseTagCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseTagRepository(db)

    async def execute(self, course_id: int) -> bool:
        await self.validate(course_id=course_id)
        return True

    async def validate(self, course_id: int):
        # Получаем связанные теги курса
        course_tags = await self.repository.get_with_filters(
            filters=[self.repository.model.course_id == course_id]
        )

        # Если есть связанные теги, удаляем их
        if course_tags:
            await self.repository.delete_with_ids(ids=[tag.id for tag in course_tags])

