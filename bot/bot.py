"""Логика взаимодействия с ботом"""

import config
import client

import logging
from telethon.sync import TelegramClient, events


bot = TelegramClient(
    'bot',
    config.api_id,
    config.api_hash).start(bot_token=config.bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    """Отправка приветственного сообщения"""

    await event.reply('Привет! Я — бот, который поможет тебе составить пост с навигацией по твоему телеграм-каналу. \
                      \nПросто пришли мне ссылку на свой телеграм-канал.')
    

@bot.on(events.NewMessage(pattern='https://t\.me/(\S+)'))
async def send_tag_list(event):
    """Получаем посты из канала и возвращаем теги"""

    channel = event.text

    try:
        await client.get_channel_data(channel)
    except ValueError as error:
        if 'Cannot get entity from a channel' in str(error):
            await event.reply('Канал должен быть публичным')
        logging.error(error)

    await client.get_messages(channel)