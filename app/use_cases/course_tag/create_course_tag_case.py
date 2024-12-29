from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_tag.course_tag_dto import CourseTagRDTO, CourseTagCDTO
from app.adapters.repositories.course_tag.course_tag_repository import CourseTagRepository
from app.adapters.repositories.tag.tag_repository import TagRepository
from app.core.app_exception_response import AppExceptionResponse
from app.entities.course_tag import CourseTagModel
from app.use_cases.base_case import BaseUseCase


class CreateCourseTagCase(BaseUseCase[CourseTagRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseTagRepository(db)
        self.tag_repo = TagRepository(db)

    async def execute(self, tag_ids: list[int], course_id: int):
        for tag_id in tag_ids:
            data = {
                "tag_id": tag_id,
                "course_id": course_id
            }
            await self.repository.create(obj=CourseTagModel(**data))
        return True

    async def validate(self, tag_ids: list[int]):
        if not tag_ids:
            pass
        else:
            existing_tags = await self.tag_repo.get_all_by_ids(tag_ids)
            missing_tags = set(tag_ids) - {tag.id for tag in existing_tags}
            if missing_tags:
                raise AppExceptionResponse.bad_request(message="Тег не найден")
            return tag_ids
