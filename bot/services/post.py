"""Парсинг и запись постов в БД"""

from config import (
    client,
    session_factory as Session)

from telethon.tl.types import InputMessagesFilterEmpty

from db.models import *


async def write_posts_to_db(channel: str) -> None:
    """Парсим все текстовые посты из канала и записываем их в БД"""

    posts_list = []

    async for message in client.iter_messages(channel,
                                              reverse=True,
                                              filter=InputMessagesFilterEmpty):
        if message.text:
            posts_list.append({
                'post_id': message.id,
                'date': message.date,
                'views': message.views,
                'replies': message.replies.replies
                })
            
        if len(posts_list) == 20:
            for post in posts_list:
                print(post)

    print(posts_list)




# async def get_posts(channel: str):
#     """Парсим все текстовые посты из канала и добавляем в БД"""

#     posts_list = []
    
#     async for message in client.iter_messages(channel,
#                                               reverse=True,
#                                               filter=InputMessagesFilterEmpty):
#         if message.text:
#             message_tags = await tag.parse_tags(message.text)
#             if message_tags:
#                 print(message_tags)
#             print(message.id, message.date, message.views)
            
#         if message.replies:
#             print(message.replies.replies)