from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.answer.answer_dto import AnswerRDTO, AnswerCDTO
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.answer.all_answers_case import AllAnswersCase
from app.use_cases.answer.create_answer_case import CreateAnswerCase
from app.use_cases.answer.delete_answer_case import DeleteAnswerCase
from app.use_cases.answer.get_answer_case import GetAnswerCase
from app.use_cases.answer.update_answer_case import UpdateAnswerCase


class AnswerApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/{question_id}",
            response_model=list[AnswerRDTO],
            summary="Список ответов",
            description="Получение списка ответов",
        )(self.get_by_question)
        self.router.get(
            "/get/{id}",
            response_model=AnswerRDTO,
            summary="Получить ответ по уникальному ID",
            description="Получение ответа по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=list[AnswerRDTO],
            summary="Создать ответ",
            description="Создание ответа",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=AnswerRDTO,
            summary="Обновить ответ по уникальному ID",
            description="Обновление ответа по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить ответ по уникальному ID",
            description="Удаление ответа по уникальному идентификатору",
        )(self.delete)

    async def get_by_question(self, question_id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_ANSWER_VALUE))):
        use_case = AllAnswersCase(db)
        return await use_case.execute(question_id)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_ANSWER_VALUE))):
        use_case = GetAnswerCase(db)
        return await use_case.execute(answer_id=id)

    async def create(self, dtos: list[AnswerCDTO], db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_ANSWER_VALUE))):
        use_case = CreateAnswerCase(db)
        return await use_case.execute(dtos=dtos)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: AnswerCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_ANSWER_VALUE))
    ):
        use_case = UpdateAnswerCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_ANSWER_VALUE))
    ):
        use_case = DeleteAnswerCase(db)
        return await use_case.execute(id=id)
