"""Парсинг и преобразование тегов"""

import re
from typing import Optional, List
from sqlalchemy import select
from config import session_factory as Session
from db.models import *


async def parse_tags(post_text: str) -> Optional[List[str]]:
    """Ищем теги в сообщении и возвращаем список"""

    tag_pattern = r'#\w+'
    tags_list = re.findall(tag_pattern,
                           post_text)

    if not tags_list:
        return None
    
    return tags_list


async def add_tags_to_db(post_tag_list: list) -> None:
    """Добавляем теги в базу данных"""

    async with Session.begin() as session:

        for post_tag_data in post_tag_list:
            channel_id = post_tag_data['channel_id']
            post_id = post_tag_data['post_id']
            tags_list = post_tag_data['tags_list']

            channel_pk = await session.scalar(select(Channel)
                                             .where(Channel.channel_id == channel_id))
            
            post_pk = await session.scalar(select(Post)
                                       .where(Post.channel == channel_pk,
                                              Post.post_id == post_id))
            
            for tag_name in tags_list:
                tag = Tag(name=tag_name)
                tag.channels.append(channel_pk)
                tag.posts.append(post_pk)
                session.add(tag)


async def get_tags_list(channel_data: dict):
    """Получаем теги определенного канала из БД"""

    async with Session.begin() as session:
        # channel_pk = await session.scalar(select(Channel)
        #                                      .where(Channel.id == channel_data['id']))
        tags_query = select(Tag.name).where(Tag.channels.any(Channel.id == channel_data['id']))
        tags_result = await session.execute(tags_query)
        tags = tags_result.all()
    
        print(f'!!!!!СПИСОК ТЕГОВ!!!!!! {tags}')