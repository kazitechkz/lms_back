from app.adapters.api.permission_api import PermissionApi
from app.adapters.api.role_api import RoleApi


def include_routers(app) -> None:
    app.include_router(RoleApi().router, prefix="/role", tags=["role"])
    app.include_router(PermissionApi().router, prefix="/permission", tags=["permission"])
