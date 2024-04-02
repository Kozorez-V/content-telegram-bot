"""Создание клавиатур для бота"""

from telethon.tl.custom import InlineKeyboardButton, InlineKeyboardMarkup


async def create_tags_keyboard(tags: list):
    """Создание клавиатуры со списком тегов"""

    keyboard = []
    for tag in tags:
        button = InlineKeyboardButton(tag, callback_data=tag)
        keyboard.append([button])
    print(type(InlineKeyboardMarkup(keyboard)))
    return InlineKeyboardMarkup(keyboard)