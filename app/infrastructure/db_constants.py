from datetime import date, datetime
from typing import Annotated, Optional

from fastapi import Path
from pydantic import EmailStr, Field
from sqlalchemy import Date, Numeric, String, Text, text, Integer, ForeignKey, Boolean
from sqlalchemy.dialects.mssql import JSON
from sqlalchemy.orm import mapped_column


class AppTableNames:
    # TableNames
    RoleTableName = "roles"
    PermissionTableName = "permissions"
    RolePermissionTableName = "role_permissions"
    LanguageTableName = "languages"
    UserTypeTableName = "user_types"
    OrganizationTypeTableName = "organization_types"
    CourseCategoryTableName = "course_categories"
    CourseTypeTableName = "course_types"
    TagTableName = "tags"
    QuestionTableName = "questions"
    QuestionTypeTableName = "question_types"
    CharacteristicTableName = "characteristics"
    OrganizationTableName = "organizations"
    TestTableName = "tests"
    FeedbackTableName = "feedbacks"
    AnswerTableName = "answers"
    MaterialTableName = "materials"
    CourseMaterialTableName = "course_materials"
    VideoMaterialTableName = "video_materials"
    TokenTableName = "tokens"
    CourseTableName = "courses"
    VideoCourseTableName = "video_courses"
    CourseTagTableName = "course_tags"
    UserTableName = "users"
    FileTableName = "files"

    # Model Names
    RoleModelName = "RoleModel"
    PermissionModelName = "PermissionModel"
    RolePermissionModelName = "RolePermissionModel"
    LanguageModelName = "LanguageModel"
    UserTypeModelName = "UserTypeModel"
    OrganizationModelName = "OrganizationModel"
    OrganizationTypeModelName = "OrganizationTypeModel"
    CourseCategoryModelName = "CourseCategoryModel"
    CourseTypeModelName = "CourseTypeModel"
    TagModelName = "TagModel"
    FeedbackModelName = "FeedbackModel"
    QuestionModelName = "QuestionModel"
    QuestionTypeModelName = "QuestionTypeModel"
    TestModelName = "TestModel"
    AnswerModelName = "AnswerModel"
    MaterialModelName = "MaterialModel"
    TokenModelName = "TokenModel"
    CourseModelName = "CourseModel"
    CourseMaterialModelName = "CourseMaterialModel"
    CharacteristicModel = "CharacteristicModel"
    VideoMaterialModelName = "VideoMaterialModel"
    VideoCourseModelName = "VideoCourseModel"
    CourseTagModelName = "CourseTagModel"
    UserModelName = "UserModel"
    FileModelName = "FileModel"


class AppDbValueConstants:
    # roles
    ADMINISTRATOR_VALUE = "administrator"
    MODERATOR_VALUE = "moderator"
    COMPANY_LEAD_VALUE = "company_lead"
    COMPANY_MANAGER_VALUE = "company_manager"
    EMPLOYEE_VALUE = "employee"
    # Роли, которые нельзя удалить или изменить
    IMMUTABLE_ROLES = frozenset(
        [
            ADMINISTRATOR_VALUE,
            MODERATOR_VALUE,
            COMPANY_LEAD_VALUE,
            COMPANY_MANAGER_VALUE,
            EMPLOYEE_VALUE,
        ]
    )
    # Languages
    RUSSIAN_VALUE = "ru"
    KAZAKH_VALUE = "kk"
    ENGLISH_VALUE = "en"
    IMMUTABLE_LANGUAGES = frozenset(
        [
            RUSSIAN_VALUE,
            KAZAKH_VALUE,
            ENGLISH_VALUE,
        ]
    )

    # CourseTypes
    PAID_VALUE = "paid"
    PRIVATE_VALUE = "private"
    FREE_VALUE = "free"
    IMMUTABLE_COURSE_TYPES = frozenset(
        [
            PAID_VALUE,
            PRIVATE_VALUE,
            FREE_VALUE
        ]
    )
    # UserTypes
    INDIVIDUAL_VALUE = "individual"
    LEGAL_VALUE = "legal"
    IMMUTABLE_USER_TYPES = frozenset(
        [
            INDIVIDUAL_VALUE,
            LEGAL_VALUE,
        ]
    )
    # Organization Types
    LLP_VALUE = "llp"
    IE_VALUE = "ie"
    JCS_VALUE = "jcs"
    SC_VALUE = "sc"
    FE_VALUE = "fe"
    PC_VALUE = "pc"
    NON_JCS_VALUE = "non_jcs"
    IMMUTABLE_ORGANIZATION_TYPES = frozenset(
        [
            LLP_VALUE,
            IE_VALUE,
            JCS_VALUE,
            SC_VALUE,
            FE_VALUE,
            PC_VALUE,
            NON_JCS_VALUE,
        ]
    )


class FieldConstants:
    # Columns
    STANDARD_LENGTH = 256
    STANDARD_TEXT = 1000
    STANDARD_LONG_TEXT = 2000
    PRICE_PRECISION = 10
    PRICE_SCALE = 2
    IIN_LENGTH = 12
    BIN_LENGTH = 12
    UNIQUE_PAYMENT_LENGTH = 100
    SHORT_LENGTH = 50


class ColumnConstants:
    ID = Annotated[int, mapped_column(primary_key=True)]
    # ForeignKey унификации с onupdate и ondelete
    ForeignKeyInteger = (
        lambda table_name, onupdate=None, ondelete=None, foreign_column="id": Annotated[
            int,
            mapped_column(
                Integer(),
                ForeignKey(
                    f"{table_name}.{foreign_column}",
                    onupdate=onupdate,
                    ondelete=ondelete,
                ),
                nullable=False,
            ),
        ]
    )
    ForeignKeyNullableInteger = (
        lambda table_name, onupdate=None, ondelete=None, foreign_column="id": Annotated[
            Optional[int],
            mapped_column(
                Integer(),
                ForeignKey(
                    f"{table_name}.{foreign_column}",
                    onupdate=onupdate,
                    ondelete=ondelete,
                ),
                nullable=True,
            ),
        ]
    )

    ForeignKeyString = (
        lambda table_name, onupdate=None, ondelete=None, foreign_column="id": Annotated[
            str,
            mapped_column(
                String(length=255),
                ForeignKey(
                    f"{table_name}.{foreign_column}",
                    onupdate=onupdate,
                    ondelete=ondelete,
                ),
                nullable=False,
            ),
        ]
    )
    ForeignKeyNullableString = (
        lambda table_name, onupdate=None, ondelete=None, foreign_column="id": Annotated[
            Optional[str],
            mapped_column(
                String(length=255),
                ForeignKey(
                    f"{table_name}.{foreign_column}",
                    onupdate=onupdate,
                    ondelete=ondelete,
                ),
                nullable=True,
            ),
        ]
    )
    CreatedAt = Annotated[
        datetime, mapped_column(server_default=text("CURRENT_TIMESTAMP"))
    ]
    UpdatedAt = Annotated[
        datetime,
        mapped_column(
            server_default=text("CURRENT_TIMESTAMP"), onupdate=datetime.now()
        ),
    ]

    # Аннотации для JSON полей
    JsonField = Annotated[
        dict, mapped_column(JSON)
    ]

    JsonNullableField = Annotated[
        dict, mapped_column(JSON, nullable=True)
    ]

    # Аннотации для стандартных типов
    StandardVarchar = Annotated[
        str, mapped_column(String(length=FieldConstants.STANDARD_LENGTH))
    ]
    StandardNullableVarchar = Annotated[
        str, mapped_column(String(length=FieldConstants.STANDARD_LENGTH), nullable=True)
    ]
    StandardUniqueEmail = Annotated[
        str,
        mapped_column(
            String(length=FieldConstants.STANDARD_LENGTH), unique=True, index=True
        ),
    ]
    StandardUniquePhone = Annotated[
        str,
        mapped_column(
            String(length=FieldConstants.STANDARD_LENGTH), unique=True, index=True
        ),
    ]
    StandardUniqueValue = Annotated[
        str,
        mapped_column(
            String(length=FieldConstants.STANDARD_LENGTH), unique=True, index=True
        ),
    ]
    StandardNullableText = Annotated[str, mapped_column(Text(), nullable=True)]
    StandardText = Annotated[str, mapped_column(Text())]
    StandardPrice = Annotated[
        float,
        mapped_column(
            Numeric(
                precision=FieldConstants.PRICE_PRECISION,
                scale=FieldConstants.PRICE_SCALE,
            )
        ),
    ]
    StandardNullablePrice = Annotated[
        Optional[float],
        mapped_column(
            Numeric(
                precision=FieldConstants.PRICE_PRECISION,
                scale=FieldConstants.PRICE_SCALE,
            ),
            nullable=True,
        ),
    ]

    StandardNullableDate = Annotated[
        Optional[date], mapped_column(Date(), nullable=True)
    ]
    StandardDate = Annotated[date, mapped_column(Date())]

    StandardInteger = Annotated[int, mapped_column(Integer())]
    StandardNullableInteger = Annotated[Optional[int], mapped_column(Integer(), nullable=True)]

    StandardBool = Annotated[bool, mapped_column(Boolean(), default=False)]

class DTOConstant:
    StandardID = Annotated[int, Field(description="Уникальный идентификатор")]

    StandardTitleRu = Annotated[
        str,
        Field(
            max_length=FieldConstants.STANDARD_LENGTH,
            description="Наименование на русском языке",
        ),
    ]

    StandardTitleKk = Annotated[
        str,
        Field(
            max_length=FieldConstants.STANDARD_LENGTH,
            description="Наименование на казахском языке",
        ),
    ]

    StandardTitleEn = Annotated[
        Optional[str],
        Field(
            max_length=FieldConstants.STANDARD_LENGTH,
            description="Наименование на английском языке",
        ),
    ]

    StandardValue = Annotated[
        str,
        Field(
            max_length=FieldConstants.STANDARD_LENGTH,
            description="Уникальное значение",
        ),
    ]

    StandardVarchar = Annotated[
        str,
        Field(
            max_length=FieldConstants.STANDARD_LENGTH,
            description="Строковое поле до 256 символов",
        ),
    ]

    StandardInteger = Annotated[
        int,
        Field(
            description="Стандартное цифровое поле",
        ),
    ]

    StandardBoolean = Annotated[
        bool,
        Field(
            description="Стандартное bool поле",
        ),
    ]

    StandardText = Annotated[
        str,
        Field(
            max_length=FieldConstants.STANDARD_TEXT,
            description="Строковое поле до 1000 символов",
        ),
    ]

    StandardCreatedAt = Annotated[datetime, Field(description="Дата создания")]

    StandardUpdatedAt = Annotated[datetime, Field(description="Дата обновления")]


class PathConstants:
    IDPath = Annotated[int, Path(gt=0, description="Уникальный идентификатор")]
    ValuePath = Annotated[
        str,
        Path(
            max_length=FieldConstants.STANDARD_LENGTH, description="Уникальное значение"
        ),
    ]
