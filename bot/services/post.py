"""Парсинг и запись постов в БД"""

import datetime
from sqlalchemy import select
from telethon.tl.types import InputMessagesFilterEmpty
from db.models import *
from services.tag import parse_tags, add_tags_to_db
from services.channel import delete_channel_from_db
from config import (
    client,
    session_factory as Session)


async def parse_posts(channel: str, channel_data: dict) -> None:
    """
    Парсим все текстовые посты из канала и записываем в БД каждые 20 постов.
    Если общее количество постов меньше 20, сразу записываем их в БД.
    """

    posts_list = []
    post_tag_list = []
    posts_with_tags = 0

    async for post in client.iter_messages(channel,
                                              reverse=True,
                                              filter=InputMessagesFilterEmpty):
        
        if post.text:
            # Вносим данные поста в словарь

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

            # Вносим словарь в список постов
                
            posts_list.append(post_data)

            # Парсим теги

            tags_list = await parse_tags(post.text)

            # Увеличиваем счетчик постов с тегами

            if tags_list:
                posts_with_tags += 1

            # Запоминаем текущие данные для сохранения тегов в БД 

                post_tag_data = {
                    'post_id': int(post.id),
                    'channel_id': channel_data['id'],
                    'tags_list': tags_list
                }

                post_tag_list.append(post_tag_data)

        # Записываем посты и теги в БД

        # Если набралось 20 постов с тегами,
        # записываем их в БД и очищаем списки для следующей порции

        if len(posts_list) == 20 and posts_with_tags > 0:

            await add_posts_to_db(posts_list, channel_data)
            await add_tags_to_db(post_tag_list)
            
            posts_list.clear()
            post_tag_list.clear()

        # Если набралось 20 постов без тегов,
        # очищаем список постов и продолжаем парсинг

        elif len(posts_list) == 20 and posts_with_tags == 0:

            posts_list.clear()

    # Запись в БД и очищение списков, если постов с тегами меньше 20

    if posts_list and posts_with_tags > 0:

        await add_posts_to_db(posts_list, channel_data)
        await add_tags_to_db(post_tag_list)

        posts_list.clear()
        post_tag_list.clear()

    # Поднимаем исключение, если теги не найдены
        
    if posts_with_tags == 0:
         
         await delete_channel_from_db(channel_data)
         
         raise ValueError('Не найдено ни одного тега')


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