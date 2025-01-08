from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.pagination_dto import PaginationQuestions
from app.adapters.dto.question.question_dto import QuestionRDTO, QuestionCDTO, QuestionUDTO, QuestionRDTOWithRelated
from app.adapters.filters.question.question_filter import QuestionFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.question.all_question_case import AllQuestionsCase
from app.use_cases.question.create_question_case import CreateQuestionCase
from app.use_cases.question.delete_question_case import DeleteQuestionCase
from app.use_cases.question.get_question_by_test_case import GetQuestionByTestCase
from app.use_cases.question.get_question_case import GetQuestionCase
from app.use_cases.question.update_question_case import UpdateQuestionCase


class QuestionApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=PaginationQuestions,
            summary="Список вопросов",
            description="Получение списка вопросов",
        )(self.get_all)
        self.router.get(
            "/get-by-test/{test_id}",
            response_model=list[QuestionRDTO],
            summary="Получить вопрос по уникальному ID",
            description="Получение вопроса по уникальному идентификатору",
        )(self.get_by_test)
        self.router.get(
            "/get/{id}",
            response_model=QuestionRDTOWithRelated,
            summary="Получить вопрос по уникальному ID",
            description="Получение вопроса по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=QuestionRDTO,
            summary="Создать вопрос",
            description="Создание вопроса",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=QuestionRDTO,
            summary="Обновить вопрос по уникальному ID",
            description="Обновление вопроса по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить вопрос по уникальному ID",
            description="Удаление вопроса по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db), params: QuestionFilter = Depends(),
                      user=Depends(permission_dependency(PermissionConstants.READ_QUESTION_VALUE))):
        use_case = AllQuestionsCase(db=db)
        return await use_case.execute(params=params)

    async def get_by_test(self, test_id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_QUESTION_VALUE))):
        use_case = GetQuestionByTestCase(db)
        return await use_case.execute(test_id=test_id)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_QUESTION_VALUE))):
        use_case = GetQuestionCase(db)
        return await use_case.execute(question_id=id)

    async def create(self, dto: QuestionCDTO,
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_QUESTION_VALUE))):
        use_case = CreateQuestionCase(db)
        return await use_case.execute(dto=dto)

    async def update(
            self,
            id: PathConstants.IDPath,
            dto: QuestionUDTO,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_QUESTION_VALUE))
    ):
        use_case = UpdateQuestionCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
            self,
            id: PathConstants.IDPath,
            db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_QUESTION_VALUE))
    ):
        use_case = DeleteQuestionCase(db)
        return await use_case.execute(id=id)
