"""Логика взаимодействия с клиентом"""

import config
import logging
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterEmpty


client = TelegramClient('client', config.api_id, config.api_hash).start()


async def get_messages(channel):
    """Парсим все текстовые посты из канала"""
    
    async for message in client.iter_messages(channel, reverse=True, filter=InputMessagesFilterEmpty):
        if message.text:
            print(message.id, message.date, message.views, message.text)
