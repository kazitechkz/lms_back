from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.video_course.video_course_repository import VideoCourseRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.delete_file_case import DeleteFileCase


class DeleteVideoCourseCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.repository = VideoCourseRepository(db)
        self.delete_file_use_case = DeleteFileCase(db)

    async def execute(self, id: int) -> bool:
        await self.validate(id=id)
        data = await self.repository.delete(id=id)
        return data

    async def validate(self, id: int):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Видеокурс не найден")
        if existed.image is not None:
            await self.delete_file_use_case.execute(existed.image)
