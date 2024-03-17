"""Парсинг и запись постов в БД"""

import datetime

from config import (
    client,
    session_factory as Session)

from telethon.tl.types import InputMessagesFilterEmpty

from db.models import *


async def write_posts_to_db(channel: str, channel_id: int) -> None:
    """Парсим все текстовые посты из канала и записываем их в БД"""

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
            async with Session.begin() as session:
                for post_data in posts_list:
                    post = Post(post_id=post_data['post_id'],
                                date=post_data['date'],
                                views=post_data['views'],
                                replies=post_data['replies'],
                                channel_id=channel_id)
                    session.add(post)

            for number, post in enumerate(posts_list):
                print(f'Пост №{number}\n{post}')

    if posts_list:
        async with Session.begin() as session:
                for post_data in posts_list:
                    post = Post(post_id=post_data['post_id'],
                                date=post_data['date'],
                                views=post_data['views'],
                                replies=post_data['replies'],
                                channel_id=channel_id)
                    session.add(post)

        for number, post in enumerate(posts_list):
            print(f'Пост №{number}\n{post}')

