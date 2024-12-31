import os
import tempfile

from fastapi import File
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.file.file_dto import FileRDTO, FileCDTO
from app.adapters.dto.user.user_dto import UserRDTOWithRelated
from app.adapters.repositories.file.file_repository import FileRepository
from app.infrastructure.file_uploader_s3 import DocumentUploaderS3
from app.use_cases.base_case import BaseUseCase


class UploadFileCase(BaseUseCase[str]):
    def __init__(self, db: AsyncSession):
        self.uploader = DocumentUploaderS3()

    async def execute(self,
                      file: File,
                      upload_path: str = "documents/") -> str:
        obj = await self.validate(file=file, upload_path=upload_path)
        return obj

    async def validate(self, file: File, upload_path: str):

        # Создаём временный файл
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file_path = temp_file.name
            temp_file.write(await file.read())
        try:
            # Загружаем файл в S3
            s3_key = self.uploader.upload_document(file_path=temp_file_path, original_filename=file.filename,
                                                   s3_key_prefix=upload_path)

            # Генерируем предподписанный URL
            url = self.uploader.generate_presigned_url(s3_key=s3_key, expiration=3600)

            return url
        finally:
            # Удаляем временный файл после загрузки
            os.remove(temp_file_path)
