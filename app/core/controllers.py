from app.adapters.api.language_api import LanguageApi
from app.adapters.api.role_api import RoleApi


def include_routers(app) -> None:
    app.include_router(RoleApi().router, prefix="/role", tags=["role"])
    app.include_router(LanguageApi().router, prefix="/language", tags=["language"])
