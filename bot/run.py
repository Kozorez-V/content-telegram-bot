"""Запуск бота"""

import asyncio
import logging

from config import (
    engine,
    client
    )

from bot import bot

from db.models import *

loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)



async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logging.info('База данных инициализирована')


async def start() -> None:
    await init_db()

    async with bot:
        await bot.run_until_disconnected()
        logging.info('Бот запущен')

    async with client:
        await client.run_until_disconnected()
        logging.info('Клиент запущен')


if __name__ == "__main__":
    loop.create_task(start())
    loop.run_forever()

    logging.INFO
