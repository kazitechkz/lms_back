import os
import tempfile

from fastapi import File
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.file.file_dto import FileRDTO, FileCDTO
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.dto.video_course.video_course_dto import VideoCourseCDTO
from app.adapters.repositories.file.file_repository import FileRepository
from app.core.app_exception_response import AppExceptionResponse
from app.infrastructure.video_uploader_youtube import YoutubeUpload
from app.use_cases.base_case import BaseUseCase
from app.use_cases.token.get_token_case import GetTokenCase


class YoutubeUseCase(BaseUseCase[FileRDTO]):
    def __init__(self, db: AsyncSession):
        self.db = db
        self.file_repository = FileRepository(db)
        self.token_get_use_case = GetTokenCase(db)

    async def execute(self,
                      dto: VideoCourseCDTO,
                      file: File, userDTO: UserRDTOWithRelated) -> FileRDTO:
        obj = await self.validate(file=file, userDTO=userDTO, dto=dto)
        data = await self.file_repository.create(obj=obj)
        return FileRDTO.from_orm(data)

    async def validate(self, file: File,
                       dto: VideoCourseCDTO,
                       userDTO: UserRDTOWithRelated):

        # Создаём временный файл
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(await file.read())
        try:
            token = await self.token_get_use_case.execute()
            youtube_uploader = YoutubeUpload(db=self.db, access_token=token.access_token,
                                             refresh_token=token.refresh_token)
            url = await youtube_uploader.upload_video(
                file_path=temp_file_path,
                title=dto.title,
                description=dto.description,
                category_id=27
            )

            if type(url) == dict and url.get('id') is None:
                raise AppExceptionResponse.youtube_api_error(
                    user_code=url.get('user_code'),
                    device_code=url.get('device_code'),
                    verification_url=url.get('verification_url'),
                    interval=url.get('interval')
                )

            video_url = "https://www.youtube.com/watch?v=" + url.get('id')
            fileCDTO = FileCDTO(
                filename=file.filename,
                file_size=file.size,
                file_path=video_url,
                content_type=file.headers.get('content-type'),
                is_active=True,
                uploaded_by=userDTO.id,
            )
            return self.file_repository.model(**fileCDTO.dict())
        finally:
            # Удаляем временный файл после загрузки
            os.remove(temp_file_path)


