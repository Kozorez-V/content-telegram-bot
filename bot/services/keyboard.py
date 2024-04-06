"""Создание клавиатур для бота"""

from telethon.tl.custom import Button


async def create_tags_keyboard(tags: list) -> list:
    """Создание клавиатуры со списком тегов"""

    tags_keyboard = []
    for tag in tags:
        tag_button = Button.inline(text=tag, data=str(tag))
        tags_keyboard.append([tag_button])
    
    return tags_keyboard