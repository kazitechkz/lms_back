from typing import Optional

from fastapi import File
from sqlalchemy import and_
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.dto.video_course.video_course_dto import VideoCourseRDTOWithRelated, VideoCourseCDTO
from app.adapters.repositories.language.language_repository import LanguageRepository
from app.adapters.repositories.video_course.video_course_repository import VideoCourseRepository
from app.core.app_exception_response import AppExceptionResponse
from app.use_cases.base_case import BaseUseCase
from app.use_cases.file.upload_file_case import UploadFileCase
from app.use_cases.file.youtube_video_case import YoutubeUseCase


class UpdateVideoCourseCase(BaseUseCase[VideoCourseRDTOWithRelated]):
    def __init__(self, db: AsyncSession):
        self.repository = VideoCourseRepository(db)
        self.lang_repository = LanguageRepository(db)
        self.upload_file_use_case = UploadFileCase(db)
        self.youtube_video_use_case = YoutubeUseCase(db)

    async def execute(self, id: int, dto: VideoCourseCDTO,
                      user: UserRDTOWithRelated,
                      image: Optional[File] = None,
                      video: Optional[File] = None) -> VideoCourseRDTOWithRelated:
        obj = await self.validate(id=id, dto=dto)
        if image is None:
            dto.image = obj.image
        else:
            dto.image = await self.upload_file_use_case.execute(file=image, upload_path="course_images/")
        if video is None:
            dto.video_id = obj.video_id
        else:
            video = await self.youtube_video_use_case.execute(
                dto=dto, file=video, userDTO=user)
            dto.video_id = video.id
        data = await self.repository.update(obj=obj, dto=dto, options=[
            joinedload(self.repository.model.lang)
        ])
        return VideoCourseRDTOWithRelated.from_orm(data)

    async def validate(self, id: int, dto: VideoCourseCDTO):
        existed = await self.repository.get(id=id)
        if existed is None:
            raise AppExceptionResponse.not_found(message="Видеокурс не найден")
        if await self.lang_repository.get(id=dto.lang_id) is None:
            raise AppExceptionResponse.bad_request(message="Язык не найден")
        video_course = await self.repository.get_first_with_filters(filters=[
            and_(self.repository.model.level == dto.level)
        ])
        if video_course and video_course.id != id:
            raise AppExceptionResponse.bad_request(message="Курс с таким уровнем уже существует")
        return existed

