"""Запуск бота"""

import asyncio
import logging

from bot import bot
from client import client

from config import engine
# from db.models.base import Base
from db.models import *

loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        logging.info('База данных инициализирована')


async def start() -> None:
    await init_db()

    async with bot:
        await bot.run_until_disconnected()

    async with client:
        await client.run_until_disconnected()

    

if __name__ == "__main__":
    # bot.run_until_disconnected()
    # client.run_until_disconnected()
    # asyncio.run(start())

    loop.create_task(start())
    loop.run_forever()
    
    logging.INFO

    