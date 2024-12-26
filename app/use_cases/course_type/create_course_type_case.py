from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_type.course_type_dto import CourseTypeRDTO, CourseTypeCDTO
from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class CreateCourseTypeCase(BaseUseCase[CourseTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseTypeRepository(db)

    async def execute(self, dto: CourseTypeCDTO) -> CourseTypeRDTO:
        obj = await self.validate(dto=dto)
        data = await self.repository.create(obj=obj)
        return CourseTypeRDTO.from_orm(data)

    async def validate(self, dto: CourseTypeCDTO):
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value]
        ):
            raise AppExceptionResponse.bad_request(
                "Тип курса с таким значением уже существует"
            )
        return self.repository.model(**dto.dict())
