from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.dto.question_type.question_type_dto import QuestionTypeCDTO, QuestionTypeRDTO
from app.adapters.dto.tag.tag_dto import TagRDTO, TagCDTO
from app.adapters.dto.test_type.tag_type_dto import TestTypeRDTO, TestTypeCDTO
from app.core.auth_core import permission_dependency
from app.infrastructure.database import get_db
from app.infrastructure.db_constants import PathConstants
from app.infrastructure.permission_constants import PermissionConstants
from app.use_cases.question_type.all_question_types_case import AllQuestionTypesCase
from app.use_cases.question_type.create_question_type_case import CreateQuestionTypeCase
from app.use_cases.question_type.delete_question_type_case import DeleteQuestionTypeCase
from app.use_cases.question_type.get_question_type_by_value_case import GetQuestionTypeByValueCase
from app.use_cases.question_type.get_question_type_case import GetQuestionTypeCase
from app.use_cases.question_type.update_question_type_case import UpdateQuestionTypeCase
from app.use_cases.tag.all_tags_case import AllTagsCase
from app.use_cases.tag.create_tag_case import CreateTagCase
from app.use_cases.tag.delete_tag_case import DeleteTagCase
from app.use_cases.tag.get_tag_by_value_case import GetTagByValueCase
from app.use_cases.tag.get_tag_case import GetTagCase
from app.use_cases.tag.update_tag_case import UpdateTagCase
from app.use_cases.test_type.all_test_types_case import AllTestTypesCase
from app.use_cases.test_type.create_test_type_case import CreateTestTypeCase
from app.use_cases.test_type.delete_test_type_case import DeleteTestTypeCase
from app.use_cases.test_type.get_test_type_by_value_case import GetTestTypeByValueCase
from app.use_cases.test_type.get_test_type_case import GetTestTypeCase
from app.use_cases.test_type.update_test_type_case import UpdateTestTypeCase


class QuestionTypeApi:
    def __init__(self) -> None:
        self.router = APIRouter()
        self._add_routes()

    def _add_routes(self) -> None:
        self.router.get(
            "/",
            response_model=list[QuestionTypeRDTO],
            summary="Список типов вопроса",
            description="Получение списка типов вопроса",
        )(self.get_all)
        self.router.get(
            "/get/{id}",
            response_model=QuestionTypeRDTO,
            summary="Получить тип вопроса по уникальному ID",
            description="Получение типов вопроса по уникальному идентификатору",
        )(self.get)
        self.router.get(
            "/get-by-value/{value}",
            response_model=QuestionTypeRDTO,
            summary="Получить тип вопроса по уникальному значению",
            description="Получение типов вопроса по уникальному значению",
        )(self.get_by_value)
        self.router.post(
            "/create",
            response_model=QuestionTypeRDTO,
            summary="Создать тип вопроса",
            description="Создание типов вопроса",
        )(self.create)
        self.router.put(
            "/update/{id}",
            response_model=QuestionTypeRDTO,
            summary="Обновить тип вопроса по уникальному ID",
            description="Обновление типов вопроса по уникальному идентификатору",
        )(self.update)
        self.router.delete(
            "/delete/{id}",
            response_model=bool,
            summary="Удалить тип вопроса по уникальному ID",
            description="Удаление типов вопроса по уникальному идентификатору",
        )(self.delete)

    async def get_all(self, db: AsyncSession = Depends(get_db),
                      user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))):
        use_case = AllQuestionTypesCase(db)
        return await use_case.execute()

    async def get(self, id: PathConstants.IDPath, db: AsyncSession = Depends(get_db),
                  user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))):
        use_case = GetQuestionTypeCase(db)
        return await use_case.execute(question_type_id=id)

    async def get_by_value(
        self, value: PathConstants.ValuePath, db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.READ_ROLE_VALUE))
    ):
        use_case = GetQuestionTypeByValueCase(db)
        return await use_case.execute(question_type_value=value)

    async def create(self, dto: QuestionTypeCDTO, db: AsyncSession = Depends(get_db),
                     user=Depends(permission_dependency(PermissionConstants.CREATE_ROLE_VALUE))):
        use_case = CreateQuestionTypeCase(db)
        return await use_case.execute(dto=dto)

    async def update(
        self,
        id: PathConstants.IDPath,
        dto: QuestionTypeCDTO,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.UPDATE_ROLE_VALUE))
    ):
        use_case = UpdateQuestionTypeCase(db)
        return await use_case.execute(id=id, dto=dto)

    async def delete(
        self,
        id: PathConstants.IDPath,
        db: AsyncSession = Depends(get_db),
            user=Depends(permission_dependency(PermissionConstants.DELETE_ROLE_VALUE))
    ):
        use_case = DeleteQuestionTypeCase(db)
        return await use_case.execute(id=id)
