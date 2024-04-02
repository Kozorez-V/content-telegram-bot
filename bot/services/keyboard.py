"""Создание клавиатур для бота"""

from telethon.tl.custom import InlineKeyboardButton, InlineKeyboardMarkup


def create_tags_keyboard(tags):
    keyboard = []
    for tag in tags:
        button = InlineKeyboardButton(tag, callback_data=tag)
        keyboard.append([button])
    return InlineKeyboardMarkup(keyboard)