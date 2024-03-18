"""Парсинг и запись постов в БД"""

import datetime
from sqlalchemy import select

from config import (
    client,
    session_factory as Session)

from telethon.tl.types import InputMessagesFilterEmpty

from db.models import *


async def parse_posts(channel: str, channel_data: dict) -> None:
    """
    Парсим все текстовые посты из канала и записываем в БД каждые 20 постов.
    Если общее количество постов меньше 20, сразу записываем их в БД.
    """

    posts_list = []

    async for post in client.iter_messages(channel,
                                              reverse=True,
                                              filter=InputMessagesFilterEmpty):
        if post.text:
            post_data = {
                'post_id': int(post.id),
                'date': datetime.datetime(post.date.year,
                                          post.date.month,
                                          post.date.day),
                'views': post.views,
                'replies': 0,
            }

            if post.replies:
                post_data['replies'] = post.replies.replies

            posts_list.append(post_data)

        if len(posts_list) == 20:
            await add_post_to_db(posts_list, channel_data)
            posts_list.clear()

    if posts_list:
        await add_post_to_db(posts_list, channel_data)


async def add_post_to_db(posts_list: list, channel_data) -> None:
    """Добавляем посты в базу данных"""

    async with Session.begin() as session:
                channel_pk = await session.scalar(select(Channel)
                                             .where(Channel.username == channel_data['username']))
                
                for post_data in posts_list:
                    post = Post(post_id=post_data['post_id'],
                                date=post_data['date'],
                                views=post_data['views'],
                                replies=post_data['replies'],
                                channel=channel_pk)
                    session.add(post)