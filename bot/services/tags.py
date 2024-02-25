"""Парсинг и преобразование тегов"""

import re
from typing import Optional, List

async def parse_tags(message_text: str) -> Optional[List[str]]:
    """Ищем теги в сообщении и возвращаем список"""
    tag_pattern = r'#\w+'
    tags_list = re.findall(tag_pattern,
                           message_text)

    if not tags_list:
        return None
    
    return tags_list