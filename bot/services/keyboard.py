"""Создание клавиатур для бота"""

from telethon.tl.custom import Button


async def create_tags_keyboard(tags: tuple) -> list:
    """Создание клавиатуры со списком тегов"""

    tags_keyboard = []
    for tag_name, tag_id in tags:
        tag_button = Button.inline(text=tag_name, data=tag_id)
        tags_keyboard.append([tag_button])
    
    return tags_keyboard