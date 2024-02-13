"""Логика взаимодействия с клиентом"""

import loader

from telethon.sync import TelegramClient


client = TelegramClient('client', loader.api_id, loader.api_hash).start()


async def get_messages(channel):
    """Парсим все посты из канала"""

    async for message in client.iter_messages(channel):
        print(message)