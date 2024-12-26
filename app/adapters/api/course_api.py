from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course.course_dto import CourseRDTO
from app.adapters.dto.pagination_dto import Pagination
from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.filters.course.course_filter import CourseFilter
from app.entities.course import CourseModel
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.course.all_courses_case import AllCoursesCase
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase


class CourseApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=Pagination[CourseRDTO],
            summary="Список ролей",
            description="Получение списка ролей",
        )(self.get_all)

    async def get_all(self, db: AsyncSession = Depends(get_db), params: CourseFilter = Depends()):
        use_case = AllCoursesCase(db=db, params=params)
        return await use_case.execute()
