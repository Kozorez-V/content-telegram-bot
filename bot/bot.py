"""Логика взаимодействия с ботом"""

from config import bot
import client

import logging
from telethon.sync import events


@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event) -> None:
    """Отправка приветственного сообщения"""

    await event.reply('Привет! Я — бот, который поможет тебе составить пост с навигацией по твоему телеграм-каналу. \
                      \nПросто пришли мне ссылку на свой телеграм-канал.')
    

@bot.on(events.NewMessage(pattern='https://t\.me/(\S+)'))
async def send_tag_list(event) -> None:
    """Получаем посты из канала и возвращаем теги"""

    channel = event.text

    try:
        channel_data = await client.get_channel_data(channel)
    except ValueError as error:
        if 'Cannot get entity from a channel' in str(error):
            await event.reply('Канал должен быть публичным')
        logging.error(error)

    await client.add_channel_to_db(channel_data)