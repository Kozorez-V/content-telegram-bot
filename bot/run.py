"""Запуск бота"""

import asyncio
import logging

from bot import bot
from client import client

from config import engine
from db.models.base import Base
from db.models import *


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        logging.INFO


if __name__ == "__main__":
    bot.run_until_disconnected()
    client.run_until_disconnected()
    asyncio.run(init_db())
    
    logging.INFO

    