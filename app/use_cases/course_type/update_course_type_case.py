from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.course_type.course_type_dto import CourseTypeRDTO, CourseTypeCDTO
from app.adapters.dto.role.role_dto import RoleCDTO
from app.adapters.repositories.course_type.course_type_repository import CourseTypeRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase


class UpdateCourseTypeCase(BaseUseCase[CourseTypeRDTO]):
    def __init__(self, db: AsyncSession):
        self.repository = CourseTypeRepository(db)

    async def execute(self, id: int, dto: RoleCDTO) -> CourseTypeRDTO:
        obj = await self.validate(id=id, dto=dto)
        data = await self.repository.update(obj=obj, dto=dto)
        return CourseTypeRDTO.from_orm(data)

    async def validate(self, id: int, dto: CourseTypeCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Тип курса не найден")
        if await self.repository.get_first_with_filters(
            [self.repository.model.value == dto.value, self.repository.model.id != id]
        ):
            raise AppExceptionResponse.bad_request(
                "Тип курса с таким значением уже существует"
            )
        return existed
