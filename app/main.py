from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from infrastructure.config import app_config
from starlette.staticfiles import StaticFiles

from app.core.controllers import include_routers
from app.seeders.runner import run_seeders


@asynccontextmanager
async def lifespan(app: FastAPI):
    await run_seeders()
    yield


app = FastAPI(
    title=app_config.app_name,
    description=app_config.app_description,
    version=app_config.app_version,
    lifespan=lifespan,
    debug=True,
    docs_url=app_config.app_docs_url,
    redoc_url=None,
)

# Включаем все роутеры
include_routers(app)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Запуск сервера
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
