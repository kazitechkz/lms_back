from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.answer.answer_dto import AnswerRDTO, AnswerCDTO
from app.adapters.dto.feedback.feedback_dto import FeedbackRDTOWithRelated, FeedbackCDTO
from app.adapters.dto.pagination_dto import PaginationFeedbacks
from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.filters.feedback.feedback_filter import FeedbackFilter
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.answer.all_answers_case import AllAnswersCase
from app.use_cases.answer.create_answer_case import CreateAnswerCase
from app.use_cases.answer.delete_answer_case import DeleteAnswerCase
from app.use_cases.answer.get_answer_case import GetAnswerCase
from app.use_cases.answer.update_answer_case import UpdateAnswerCase
from app.use_cases.feedback.all_feedbacks_case import AllFeedbacksCase
from app.use_cases.feedback.create_feedback_case import CreateFeedbackCase
from app.use_cases.feedback.delete_feedback_case import DeleteFeedbackCase
from app.use_cases.feedback.get_feedback_case import GetFeedbackCase
from app.use_cases.feedback.update_feedback_case import UpdateFeedbackCase
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase


class FeedbackApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/{question_id}",
            response_model=PaginationFeedbacks,
            summary="Список обращений",
            description="Получение списка обращений",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=FeedbackRDTOWithRelated,
            summary="Получить обращение по уникальному ID",
            description="Получение обращении по уникальному идентификатору",
        )(self.get)
        self.router.post(
            "/create",
            response_model=FeedbackRDTOWithRelated,
            summary="Создать обращение",
            description="Создание обращении",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=FeedbackRDTOWithRelated,
            summary="Обновить обращение по уникальному ID",
            description="Обновление обращении по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить обращение по уникальному ID",
            description="Удаление обращении по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      params: FeedbackFilter = Depends(),
                      user=Depends(permission_dependency(PermissionConstants.READ_FEEDBACK_VALUE))):
        use_case = AllFeedbacksCase(db)
        return await use_case.execute(params)

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_FEEDBACK_VALUE))):
        use_case = GetFeedbackCase(db)
        return await use_case.execute(feedback_id=id)

    async def create(self, dto: FeedbackCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_FEEDBACK_VALUE))):
        use_case = CreateFeedbackCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: FeedbackCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_FEEDBACK_VALUE))
    ):
        use_case = UpdateFeedbackCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_FEEDBACK_VALUE))
    ):
        use_case = DeleteFeedbackCase(db)
        return await use_case.execute(id=id)
