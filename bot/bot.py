"""Логика взаимодействия с ботом"""

import logging
from telethon.sync import TelegramClient, events

from services import (
    channel,
    post,
    tag
)

from config import (
    api_id,
    api_hash,
    bot_token
)


bot = TelegramClient(
    'bot',
    api_id,
    api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event) -> None:
    """Отправка приветственного сообщения"""

    await event.reply('Привет! Я — бот, который поможет тебе составить пост с навигацией по твоему телеграм-каналу. \
                      \nПросто пришли мне ссылку на свой телеграм-канал.')
    

@bot.on(events.NewMessage(pattern='https://t\.me/(\S+)'))
async def send_tag_list(event) -> None:
    """Получаем посты из канала и возвращаем теги"""

    channel_link = event.text

    try:
        channel_data = await channel.get_channel_data(channel_link)
    except ValueError as error:
        if 'Cannot get entity from a channel' in str(error):
            await event.reply('Канал должен быть публичным')
        logging.error(error)

    try:
        await channel.add_channel_to_db(channel_data)
    except Exception as error:
        logging.error(error)
        
    await post.write_posts_to_db(channel_link)

