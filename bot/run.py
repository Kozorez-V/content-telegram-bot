"""Запуск бота"""

import asyncio
import logging

from bot import bot
from client import client

import config
from db.models.base import Base

async def async_main() -> None:
    async with config.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    bot.run_until_disconnected()
    client.run_until_disconnected()

    asyncio.run(async_main())
    logging.INFO

    