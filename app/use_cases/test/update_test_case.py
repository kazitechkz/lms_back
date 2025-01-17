from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.test.test_dto import TestRDTO, TestCDTO
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.organization.organization_repository import OrganizationRepository
from app.adapters.repositories.test.test_repository import TestRepository
from app.adapters.repositories.video_course.video_course_repository import VideoCourseRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateTestCase(BaseUseCase[TestRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = TestRepository(db)
        self.course_repository = CourseRepository(db)
        self.video_repository = VideoCourseRepository(db)
        self.organization_repository = OrganizationRepository(db)

    async def execute(self, id: int, dto: TestCDTO) -> TestRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return TestRDTO.from_orm(data)

    async def validate(self, id: int, dto: TestCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Тест не найден")
        if dto.course_id:
            if await self.course_repository.get(id=dto.course_id) is None:
                raise AppExceptionResponse.bad_request(message="Курс не найден")
        if dto.video_id:
            if await self.video_repository.get(id=dto.video_id) is None:
                raise AppExceptionResponse.bad_request(message="Видеокурс не найден")
        if dto.organization_id:
            if await self.organization_repository.get(id=dto.organization_id) is None:
                raise AppExceptionResponse.bad_request(message="Организация не найдена")

        return existed
