from fastapi import File
from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.dto.video_course.video_course_dto import VideoCourseRDTOWithRelated, VideoCourseCDTO
from app.adapters.repositories.course.course_repository import CourseRepository
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.adapters.repositories.video_course.video_course_repository import VideoCourseRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.upload_file_case import UploadFileCase
from app.use_cases.file.youtube_video_case import YoutubeUseCase


class CreateVideoCourseCase(BaseUseCase[VideoCourseRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = VideoCourseRepository(db)
        self.lang_repository = LanguageRepository(db)
        self.course_repository = CourseRepository(db)
        self.upload_file_use_case = UploadFileCase(db)
        self.youtube_video_use_case = YoutubeUseCase(db)

    async def execute(self, dto: VideoCourseCDTO, file: File, user: UserRDTOWithRelated, video: File):
        obj = await self.validate(dto=dto, image=file, user=user, video=video)
        data = await self.repository.create(obj=obj, options=[
            joinedload(self.repository.model.course),
            joinedload(self.repository.model.video),
            joinedload(self.repository.model.lang)
        ])
        return VideoCourseRDTOWithRelated.from_orm(data)

    async def validate(self, dto: VideoCourseCDTO, image: File, video: File, user: UserRDTOWithRelated):
        if await self.course_repository.get(id=dto.course_id) is None:
            raise AppExceptionResponse.bad_request(message="Курс не найден")
        if await self.lang_repository.get(id=dto.lang_id) is None:
            raise AppExceptionResponse.bad_request(message="Язык не найден")
        video_course = await self.repository.get_first_with_filters(filters=[
            and_(self.repository.model.level == dto.level, self.repository.model.lang_id == dto.lang_id)
        ])
        if video_course is not None:
            raise AppExceptionResponse.bad_request(message="Курс с таким уровнем и языком уже существует")
        if image is None:
            raise AppExceptionResponse.bad_request(message="Необходимо загрузить обложку и видео")
        if video:
            video = await self.youtube_video_use_case.execute(
                dto=dto, file=video, userDTO=user, upload_path="course_videos/")
            dto.video_id = video.id
        if image:
            dto.image = await self.upload_file_use_case.execute(file=image, upload_path="course_images/")

        return self.repository.model(**dto.dict())
