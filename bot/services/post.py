"""Парсинг и запись постов в БД"""

from ..config import (
    client,
    session_factory as Session)

from telethon.tl.types import InputMessagesFilterEmpty
from services import tag

from db.models import *


async def get_posts(channel: str):
    """Парсим все текстовые посты из канала и добавляем в БД"""
    
    async for message in client.iter_messages(channel,
                                              reverse=True,
                                              filter=InputMessagesFilterEmpty):
        if message.text:
            message_tags = await tag.parse_tags(message.text)
            if message_tags:
                print(message_tags)
            # print(message.id, message.date, message.views)
            
        # if message.replies:
        #     print(message.replies.replies)