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


async def add_tags_to_db(tags_list: list, channel_data: dict) -> None:
    """Добавляем теги в базу данных"""

    async with Session.begin() as session:
        channel_pk = await session.scalar(select(Channel)
                                             .where(Channel.username == channel_data['username']))
        
        for tag_data in tags_list:
            tag = Tag(name=tag_data)
            tag.channels.append(channel_pk)
            session.add(tag)