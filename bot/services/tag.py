"""Парсинг и преобразование тегов"""

import re
from typing import Optional, List
from sqlalchemy import select
from config import session_factory as Session
from db.models import *

import logging


async def parse_tags(post_text: str) -> Optional[List[str]]:
    """Ищем теги в сообщении и возвращаем список"""

    tag_pattern = r'#\w+'
    tags_list = re.findall(tag_pattern,
                           post_text)

    if not tags_list:
        return None
    
    return tags_list


async def add_tags_to_db(tags_list: list, channel_data: dict, post_id: int) -> None:
    """Добавляем теги в базу данных"""

    async with Session.begin() as session:
        channel_pk = await session.scalar(select(Channel)
                                             .where(Channel.username == channel_data['username']))
        
        post_pk = await session.scalar(select(Post)
                                       .where(Post.channel == channel_pk,
                                              Post.post_id == post_id))
        
        for tag_name in tags_list:
            tag = Tag(name=tag_name)
            tag.channels.append(channel_pk)
            tag.posts.append(post_pk)
            session.add(tag)