"""Парсинг и запись постов в БД"""

import datetime
from sqlalchemy import select
from telethon.tl.types import InputMessagesFilterEmpty
from db.models import *
from services import tag
from config import (
    client,
    session_factory as Session)


async def parse_posts(channel: str, channel_data: dict) -> None:
    """
    Парсим все текстовые посты из канала и записываем в БД каждые 20 постов.
    Если общее количество постов меньше 20, сразу записываем их в БД.
    """

    posts_list = []
    posts_with_tags = 0

    async for post in client.iter_messages(channel,
                                              reverse=True,
                                              filter=InputMessagesFilterEmpty):
        if post.text:
            tags_list = await tag.parse_tags(post.text)

            if tags_list:
                posts_with_tags += 1
                await tag.add_tags_to_db(tags_list, channel_data)

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
            await add_posts_to_db(posts_list, channel_data)
            posts_list.clear()
        
    if posts_with_tags == 0:
         raise ValueError('Не найдено ни одного тега')

    if posts_list:
        await add_posts_to_db(posts_list, channel_data)


async def add_posts_to_db(posts_list: list, channel_data: dict) -> None:
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