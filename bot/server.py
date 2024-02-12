"""Логика взаимодействия с телеграм-ботом"""

from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetMessagesViewsRequest
from telethon.tl.types import InputPeerChannel
from dotenv import load_dotenv
import os

# Загрузка переменных из окружения
load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

client = TelegramClient('client', api_id, api_hash).start()
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

@bot.on(events.NewMessage(pattern='/start'))
async def send_welcome(event):
    """Отправка приветственного сообщения"""

    await event.reply('Привет! Я — бот, который поможет тебе составить пост с навигацией по твоему телеграм-каналу. \
                      \n Просто пришли мне ссылку на твой телеграм-канал.')
    

@bot.on(events.NewMessage(pattern='https://t\.me/(\w+)'))
async def send_tag_list(event):
    """Получаем посты из канала и возвращаем теги"""
    async for message in client.iter_messages(event):
        print(message)


if __name__ == "__main__":
    bot.run_until_disconnected()
    client.run_until_disconnected()