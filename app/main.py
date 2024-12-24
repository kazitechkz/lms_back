from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infrastructure.config import app_config
from starlette.staticfiles import StaticFiles

from app.core.controllers import include_routers
from app.seeders.runner import run_seeders


@asynccontextmanager
async def lifespan(app: FastAPI):
    await run_seeders()
    yield

origins = [
    "http://localhost",
    "http://localhost:5173",
]


app = FastAPI(
    title=app_config.app_name,
    description=app_config.app_description,
    version=app_config.app_version,
    lifespan=lifespan,
    debug=True,
    docs_url=app_config.app_docs_url,
    redoc_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Включаем все роутеры
include_routers(app)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Запуск сервера
if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
