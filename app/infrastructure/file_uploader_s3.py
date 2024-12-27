import os
import uuid

import boto3
from botocore.exceptions import ClientError

from app.core.app_exception_response import AppExceptionResponse
from app.infrastructure.config import app_config


class DocumentUploaderS3:
    ALLOWED_EXTENSIONS = {".pdf", ".docx", ".txt", ".xlsx", ".csv", ".png", ".jpg", ".jpeg", ".webp"}
    ALLOWED_MAX_SIZE_MB = 100

    def __init__(self):
        self.bucket_name = app_config.aws_s3_bucket_name
        self.s3_client = boto3.client(
            "s3",
            aws_access_key_id=app_config.aws_access_key_id,
            aws_secret_access_key=app_config.aws_secret_access_key,
            region_name=app_config.aws_region_name,
        )

    def _generate_unique_filename(self, original_filename):
        """
        Генерация уникального имени файла на основе UUID и сохранения расширения.
        """
        ext = os.path.splitext(original_filename)[-1].lower()
        if ext not in self.ALLOWED_EXTENSIONS:
            raise AppExceptionResponse.bad_request(message=f"Файлы с расширением '{ext}' не поддерживаются.")
        unique_name = f"{uuid.uuid4()}{ext}"
        return unique_name

    def upload_document(self, file_path, original_filename, s3_key_prefix="documents/"):
        """
        Загружает документ в S3 и возвращает уникальный ключ.
        """
        try:
            filename = os.path.basename(file_path)
            unique_filename = self._generate_unique_filename(original_filename)
            s3_key = f"{s3_key_prefix}{unique_filename}"

            self.s3_client.upload_file(file_path, self.bucket_name, s3_key)
            print(
                f"Файл '{filename}' успешно загружен в '{self.bucket_name}' с ключом '{s3_key}'."
            )
            return s3_key

        except FileNotFoundError:
            print("Ошибка: Локальный файл не найден.")
            raise AppExceptionResponse.not_found(message="Ошибка: Локальный файл не найден.")
        except ClientError as e:
            print(f"Ошибка S3: {e}")
            raise AppExceptionResponse.not_found(message=f"Ошибка S3: {e}")

    def generate_presigned_url(self, s3_key, expiration=3600):
        """
        Генерация предподписанного URL для скачивания файла.
        """
        try:
            url = self.s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": self.bucket_name, "Key": s3_key},
                ExpiresIn=expiration,
            )
            print(f"Предподписанный URL: {url}")
            return url
        except ClientError as e:
            print(f"Ошибка при генерации ссылки: {e}")
            raise AppExceptionResponse.internal_error(message=f"Ошибка при генерации ссылки: {e}")
