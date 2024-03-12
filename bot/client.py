"""Логика взаимодействия с клиентом"""

import config
import logging
from telethon.sync import TelegramClient
from telethon.tl.types import InputMessagesFilterEmpty
from services import tags


client = TelegramClient(
    'client',
    config.api_id,
    config.api_hash).start()


async def get_messages(channel: str):
    """Парсим все текстовые посты из канала и добавляем в БД"""

    channel_info = await get_channel_data(channel)
    
    async for message in client.iter_messages(channel,
                                              reverse=True,
                                              filter=InputMessagesFilterEmpty):
        if message.text:
            message_tags = await tags.parse_tags(message.text)
            if message_tags:
                print(message_tags)
            # print(message.id, message.date, message.views)
            
        # if message.replies:
        #     print(message.replies.replies)


async def get_channel_data(channel: str):
    """Получаем данные о канале"""

    channel_data = await client.get_entity(channel)

    return {
        'id': channel_data.id,
        'username': channel_data.username
    }