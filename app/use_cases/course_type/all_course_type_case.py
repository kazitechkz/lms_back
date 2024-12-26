from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_type.course_type_dto import CourseTypeRDTO
from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.use_cases.base_case import BaseUseCase


class AllCourseTypeCase(BaseUseCase[List[CourseTypeRDTO]]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseTypeRepository(db)

    async def execute(self) -> List[CourseTypeRDTO]:
        roles = await self.repository.get_all()
        return [CourseTypeRDTO.from_orm(role) for role in roles]

    async def validate(self):
        pass
