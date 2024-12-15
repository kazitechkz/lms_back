from app.infrastructure.database import AsyncSessionLocal
from app.seeders.registry import seeders


async def run_seeders():
    """Запускает все сидеры."""
    async with AsyncSessionLocal() as session:
        for seeder in seeders:
            print(f"Запуск сидера: {seeder.__class__.__name__}")
            await seeder.seed(session)
        print("Сидеры успешно выполнены.")
