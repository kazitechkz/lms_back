from app.adapters.api.answer_api import AnswerApi
from app.adapters.api.auth_api import AuthApi
from app.adapters.api.blog_api import BlogApi
from app.adapters.api.blog_category_api import BlogCategoryApi
from app.adapters.api.characteristic_api import CharacteristicApi
from app.adapters.api.course_api import CourseApi
from app.adapters.api.course_category_api import CourseCategoryApi
from app.adapters.api.course_material_api import CourseMaterialApi
from app.adapters.api.course_type_api import CourseTypeApi
from app.adapters.api.feedback_api import FeedbackApi
from app.adapters.api.file_api import FileApi
from app.adapters.api.language_api import LanguageApi
from app.adapters.api.material_api import MaterialApi
from app.adapters.api.organization_api import OrganizationApi
from app.adapters.api.permission_api import PermissionApi
from app.adapters.api.question_api import QuestionApi
from app.adapters.api.role_api import RoleApi
from app.adapters.api.role_permission_api import RolePermissionApi
from app.adapters.api.tag_api import TagApi
from app.adapters.api.test_api import TestApi
from app.adapters.api.token_api import TokenApi
from app.adapters.api.user_api import UserApi
from app.adapters.api.user_type_api import UserTypeApi
from app.adapters.api.video_course_api import VideoCourseApi
from app.adapters.api.video_material_api import VideoMaterialApi


def include_routers(app) -> None:
    app.include_router(AuthApi().router, prefix="/auth", tags=["auth"])

    app.include_router(RoleApi().router, prefix="/role", tags=["role"])
    app.include_router(RolePermissionApi().router, prefix="/role-permission", tags=["role-permission"])
    app.include_router(LanguageApi().router, prefix="/language", tags=["language"])
    app.include_router(PermissionApi().router, prefix="/permission", tags=["permission"])
    app.include_router(CourseCategoryApi().router, prefix="/course-category", tags=["course-category"])
    app.include_router(CourseTypeApi().router, prefix="/course-type", tags=["course-type"])
    app.include_router(TagApi().router, prefix="/tag", tags=["tag"])
    app.include_router(CourseApi().router, prefix="/course", tags=["course"])
    app.include_router(UserTypeApi().router, prefix="/user-type", tags=["user-type"])
    app.include_router(FileApi().router, prefix="/file", tags=["file"])
    app.include_router(UserApi().router, prefix="/user", tags=["user"])
    app.include_router(VideoCourseApi().router, prefix="/video-course", tags=["video-course"])
    app.include_router(TokenApi().router, prefix="/token", tags=["token"])
    app.include_router(MaterialApi().router, prefix="/material", tags=["material"])
    app.include_router(CourseMaterialApi().router, prefix="/course-material", tags=["course-material"])
    app.include_router(VideoMaterialApi().router, prefix="/video-material", tags=["video-material"])
    app.include_router(OrganizationApi().router, prefix="/organization", tags=["organization"])
    app.include_router(TestApi().router, prefix="/test", tags=["test"])
    app.include_router(QuestionApi().router, prefix="/question", tags=["question"])
    app.include_router(CharacteristicApi().router, prefix="/characteristic", tags=["characteristic"])
    app.include_router(AnswerApi().router, prefix="/answer", tags=["answer"])
    app.include_router(FeedbackApi().router, prefix="/feedback", tags=["feedback"])
    app.include_router(BlogCategoryApi().router, prefix="/blog-category", tags=["blog-category"])
    app.include_router(BlogApi().router, prefix="/blog", tags=["blog"])

