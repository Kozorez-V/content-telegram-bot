"""Логика взаимодействия с клиентом"""

import config
import logging
from telethon.sync import TelegramClient


client = TelegramClient('client', config.api_id, config.api_hash).start()


async def get_messages(channel):
    """Парсим все посты из канала"""

    try:
        async for message in client.iter_messages(channel):
            print(message)
    except ValueError as error:
        logging.error(error)