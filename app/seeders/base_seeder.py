import logging
from abc import ABC, abstractmethod

from sqlalchemy import func, select, text
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.config import app_config

logger = logging.getLogger(__name__)


class BaseSeeder(ABC):
    """Базовый класс для всех сидеров."""

    def __init__(self):
        self.environment = (
            app_config.app_status
        )  # Получение текущего окружения (prod/dev)
        self.db_type = app_config.db_type

    @abstractmethod
    async def seed(self, session: AsyncSession):
        """Метод для заполнения базы данных."""
        pass

    def get_data(self):
        """Загрузка данных в зависимости от окружения."""
        if self.environment == "production":
            return self.get_prod_data()
        else:
            return self.get_dev_data()

    @abstractmethod
    def get_dev_data(self):
        """Возвращает данные для разработки."""
        pass

    @abstractmethod
    def get_prod_data(self):
        """Возвращает данные для продакшена."""
        pass

    async def reset_sequence(self, session: AsyncSession, table_name: str):

        if self.db_type.startswith("postgresql"):
            await session.execute(
                text(
                    f"""
                       DO $$
                       BEGIN
                           IF EXISTS (SELECT 1 FROM {table_name}) THEN
                               PERFORM setval(pg_get_serial_sequence('{table_name}', 'id'), MAX(id)) FROM {table_name};
                           ELSE
                               PERFORM setval(pg_get_serial_sequence('{table_name}', 'id'), 1, false);
                           END IF;
                       END
                       $$;
                   """
                )
            )
            logger.info(f"Последовательность для таблицы {table_name} сброшена.")

    async def load_seeders(
        self, BaseModel, session, table_name: str, ready_data: list = None
    ):
        # Проверяем, есть ли данные в таблице
        count_query = select(func.count()).select_from(BaseModel)
        total_items = await session.scalar(count_query)

        if total_items > 0:
            logger.info(
                f"Таблица {table_name} уже содержит данные ({total_items} записей)."
            )
            return

        # Добавляем данные, если они переданы
        if ready_data:
            session.add_all(ready_data)
            await session.commit()

            # Сбрасываем последовательность для PostgreSQL
            await self.reset_sequence(session, table_name)

            print(
                f"Данные успешно добавлены в таблицу {table_name} ({len(ready_data)} записей)."
            )
