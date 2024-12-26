from app.adapters.api.course_api import CourseApi
from app.adapters.api.course_category_api import CourseCategoryApi
from app.adapters.api.course_type_api import CourseTypeApi
from app.adapters.api.language_api import LanguageApi
from app.adapters.api.permission_api import PermissionApi
from app.adapters.api.role_api import RoleApi
from app.adapters.api.tag_api import TagApi


def include_routers(app) -> None:
    app.include_router(RoleApi().router, prefix="/role", tags=["role"])
    app.include_router(LanguageApi().router, prefix="/language", tags=["language"])
    app.include_router(PermissionApi().router, prefix="/permission", tags=["permission"])
    app.include_router(CourseCategoryApi().router, prefix="/course-category", tags=["course-category"])
    app.include_router(CourseTypeApi().router, prefix="/course-type", tags=["course-type"])
    app.include_router(TagApi().router, prefix="/tag", tags=["tag"])
    app.include_router(CourseApi().router, prefix="/course", tags=["course"])
