from fastapi import APIRouter, Depends, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.auth.auth_dto import AuthCDTO
from app.adapters.dto.file.file_dto import FileRDTO
from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.use_cases.auth.auth_login_case import AuthLoginUseCase
from app.use_cases.file.create_file_case import CreateFileCase
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase


class AuthApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.post("/login")(self.login)

    async def login(self,
                     dto: AuthCDTO,
                     db: AsyncSession = Depends(get_db)):
        use_case = AuthLoginUseCase(db)
        return await use_case.execute(dto=dto)
