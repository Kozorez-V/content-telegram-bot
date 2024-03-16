"""Парсинг и запись постов в БД"""

from config import (
    client,
    session_factory as Session)

from telethon.tl.types import InputMessagesFilterEmpty

from db.models import *


async def write_posts_to_db(channel: str) -> None:
    """Парсим все текстовые посты из канала и записываем их в БД"""

    posts_list = []

    async for post in client.iter_messages(channel,
                                              reverse=True,
                                              filter=InputMessagesFilterEmpty):
        if post.text:
            post_data = {
                'post_id': post.id,
                'date': post.date.strftime("%Y-%m-%d"),
                'views': post.views,
                'replies': 0,
            }

            if post.replies:
                post_data['replies'] = post.replies.replies

            posts_list.append(post_data)

    print(len(posts_list))

    for number, post in enumerate(posts_list):
        print(f'Пост №{number}\n{post}')