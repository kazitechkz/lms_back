from app.adapters.api.role_api import RoleApi


def include_routers(app) -> None:
    app.include_router(RoleApi().router, prefix="/role", tags=["role"])
