"""Логика взаимодействия с ботом"""

import loader
import client

from telethon.sync import TelegramClient, events

bot = TelegramClient('bot', loader.api_id, loader.api_hash).start(bot_token=loader.bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    """Отправка приветственного сообщения"""

    await event.reply('Привет! Я — бот, который поможет тебе составить пост с навигацией по твоему телеграм-каналу. \
                      \n Просто пришли мне ссылку на твой телеграм-канал.')
    

@bot.on(events.NewMessage(pattern='https://t\.me/(\w+)'))
async def send_tag_list(event):
    """Получаем посты из канала и возвращаем теги"""
    
    await client.get_messages(event.text)