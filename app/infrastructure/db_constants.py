from datetime import date, datetime
from typing import Annotated, Optional

from fastapi import Path
from pydantic import EmailStr, Field
from sqlalchemy import Date, Numeric, String, Text, text, Integer
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
    UserTableName = "users"
    FileTableName = "files"

    # Model Names
    RoleModelName = "RoleModel"
    PermissionModelName = "PermissionModel"
    RolePermissionModelName = "RolePermissionModel"
    LanguageModelName = "LanguageModel"
    UserTypeModelName = "UserTypeModel"
    OrganizationModelName = "OrganizationModel"
    CourseCategoryModelName = "CourseCategoryModel"
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
    CreatedAt = Annotated[
        datetime, mapped_column(server_default=text("CURRENT_TIMESTAMP"))
    ]
    UpdatedAt = Annotated[
        datetime,
        mapped_column(
            server_default=text("CURRENT_TIMESTAMP"), onupdate=datetime.now()
        ),
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
    StandardNullableInteger = Annotated[Optional[int], mapped_column(Integer(),nullable=True)]


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
