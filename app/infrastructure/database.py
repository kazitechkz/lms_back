from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.infrastructure.config import app_config

engine_async = create_async_engine(
    app_config.get_db_url,
    echo=False,
    pool_size=app_config.db_pool_size,
    max_overflow=app_config.db_max_overflow,
    pool_timeout=app_config.db_pool_timeout,
    pool_recycle=app_config.db_pool_recycle,
)

AsyncSessionLocal = sessionmaker(
    bind=engine_async, class_=AsyncSession, expire_on_commit=False
)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()


class Base(DeclarativeBase):
    pass
