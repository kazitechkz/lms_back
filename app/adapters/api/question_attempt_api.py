from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question_attempt.question_attempt_dto import QuestionAttemptRDTO, SingleAnswerCDTO, \
    MultipleAnswerCDTO
from app.core.auth_core import get_current_user
from app.infrastructure.database import get_db
from app.use_cases.question_attempt.multiple_answer_use_case import MultipleAnswerUseCase
from app.use_cases.question_attempt.psychological_answer_use_case import PsychologicalAnswerUseCase
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
            "/pass-multiple-answer",
            response_model=QuestionAttemptRDTO,
            summary="Сдать тест по множественным ответам",
            description="Сдачи теста по множественным ответам",
        )(self.pass_multiple_answer)
        self.router.post(
            "/pass-psychological-answer",
            response_model=QuestionAttemptRDTO,
            summary="Сдать психологический тест",
            description="Сдачи психологического теста",
        )(self.pass_psychological_answer)

    async def pass_single_answer(self, db: AsyncSession = Depends(get_db), dto: SingleAnswerCDTO = Depends(),
                                 user=Depends(get_current_user)):
        use_case = SingleAnswerUseCase(db=db)
        return await use_case.execute(user=user, dto=dto)

    async def pass_multiple_answer(self, db: AsyncSession = Depends(get_db), dto: MultipleAnswerCDTO = Depends(),
                                   user=Depends(get_current_user)):
        use_case = MultipleAnswerUseCase(db=db)
        return await use_case.execute(user=user, dto=dto)

    async def pass_psychological_answer(self, db: AsyncSession = Depends(get_db), dto: MultipleAnswerCDTO = Depends(),
                                   user=Depends(get_current_user)):
        use_case = PsychologicalAnswerUseCase(db=db)
        return await use_case.execute(user=user, dto=dto)
