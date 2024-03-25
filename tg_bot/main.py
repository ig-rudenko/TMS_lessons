import asyncio
import os

from app.settings import dp, bot
from app.handlers.welcome import router as welcome_router
from app.handlers.recipes import router as recipes_router
from app.handlers.misc import router as misc_router
from app.database.connector import db_conn


async def main():
    pg_user = os.environ["POSTGRES_USER"]
    pg_password = os.environ["POSTGRES_PASSWORD"]
    pg_host = os.environ["POSTGRES_HOST"]
    pg_database = os.environ["POSTGRES_DB"]

    db_conn.initialize(f"postgresql+asyncpg://{pg_user}:{pg_password}@{pg_host}:5432/{pg_database}")

    dp.include_routers(welcome_router, recipes_router, misc_router)
    # Запуск процесса поллинга новых апдейтов
    await dp.start_polling(bot, skip_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
