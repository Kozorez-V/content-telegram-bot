"""Логика взаимодействия с клиентом"""

import config
import logging
from telethon.sync import TelegramClient
from telethon import errors



client = TelegramClient('client', config.api_id, config.api_hash).start()


async def get_messages(channel):
    """Парсим все посты из канала"""
    
    async for message in client.iter_messages(channel):
        pass
