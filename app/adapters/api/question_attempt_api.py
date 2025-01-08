from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question.question_dto import QuestionRDTO, QuestionCDTO
from app.adapters.dto.question_attempt.question_attempt_dto import QuestionAttemptRDTO, SingleAnswerCDTO
from app.core.auth_core import permission_dependency, get_current_user
from app.infrastructure.database import get_db
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.question.create_question_case import CreateQuestionCase
from app.use_cases.question_attempt.single_answer_use_case import SingleAnswerUseCase


class QuestionAttemptApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.post(
            "/pass-single-answer",
            response_model=QuestionAttemptRDTO,
            summary="Сдать тест по одинарным ответам",
            description="Сдачи теста по одинарным ответам",
        )(self.pass_single_answer)
        self.router.post(
            "/create",
            response_model=QuestionRDTO,
            summary="Создать вопрос",
            description="Создание вопроса",
        )(self.create)

    async def pass_single_answer(self, db: AsyncSession = Depends(get_db), dto: SingleAnswerCDTO = Depends(),
                                 user=Depends(get_current_user)):
        use_case = SingleAnswerUseCase(db=db)
        return await use_case.execute(user=user, dto=dto)

    async def create(self, dto: QuestionCDTO,
                     db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_QUESTION_VALUE))):
        use_case = CreateQuestionCase(db)
        return await use_case.execute(dto=dto)
