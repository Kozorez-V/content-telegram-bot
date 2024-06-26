"""Логика взаимодействия с ботом"""

import logging
import contextvars
from telethon.sync import TelegramClient, events

from services.channel import get_channel_data, add_channel_to_db
from services.post import parse_posts
from services.tag import get_tags_list
from services.keyboard import create_tags_keyboard

from config import (
    api_id,
    api_hash,
    bot_token
)

bot = TelegramClient(
    'bot',
    api_id,
    api_hash,
    sequential_updates=True).start(bot_token=bot_token)

channel_data_cv = contextvars.ContextVar('channel_data')
tags_cv = contextvars.ContextVar('tags')


@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event) -> None:
    """Отправка приветственного сообщения"""

    await event.reply('Привет! Я — бот, который поможет тебе составить пост с навигацией по твоему телеграм-каналу. \
                      \nПросто пришли мне ссылку на свой телеграм-канал.')


@bot.on(events.NewMessage(pattern='https://t\.me/(\S+)'))
async def send_tag_list(event) -> None:
    """Анализируем посты из канала и возвращаем клавиатуру с тегами"""

    channel_link = event.text

    try:
        channel_data = await get_channel_data(channel_link)
        channel_data_cv.set(channel_data)
    except ValueError as error:
        if 'Cannot get entity from a channel' in str(error):
            await event.reply('Канал должен быть публичным')
        logging.error(error)

    try:
        await add_channel_to_db(channel_data)
    except Exception as error:
        logging.error(error)

    try:
        await event.reply('Посты анализируются, ожидайте')
        await parse_posts(channel_link, channel_data)
    except ValueError as error:
        logging.error(error)
        await event.reply('К сожалению, мне не удалось найти ни одного тега')

    try:
        tags = await get_tags_list(channel_data)
        tags_cv.set(tags)
    except Exception as error:
        logging.error(error)

    tags_keyboard = await create_tags_keyboard(tags)

    await event.respond("Выберите теги", buttons=tags_keyboard)


@bot.on(events.CallbackQuery())
async def show_selected_tags(event) -> None:
    tags = tags_cv.get()

    for tag_name, tag_id in tags:
        print(f'event.data: {event.data}\ntag_id: {tag_id}')
        if int(event.data) == tag_id:
            print('Yes')
        else:
            print('No :(')
