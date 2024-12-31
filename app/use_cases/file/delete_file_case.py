from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.repositories.file.file_repository import FileRepository
from app.adapters.repositories.role.role_repository import RoleRepository
from app.core.app_exception_response import AppExceptionResponse
from app.infrastructure.db_constants import AppDbValueConstants
from app.infrastructure.file_uploader_s3 import DocumentUploaderS3
from app.use_cases.base_case import BaseUseCase


class DeleteFileCase(BaseUseCase[bool]):
    def __init__(self, db: AsyncSession):
        self.file_repository = FileRepository(db)
        self.uploader = DocumentUploaderS3()

    async def execute(self, url: str) -> bool:
        self.validate(url=url)
        self.uploader.delete_document_by_url(url)
        return True

    def validate(self, url: str):
        if url is None:
            raise AppExceptionResponse.bad_request(message="Invalid")
