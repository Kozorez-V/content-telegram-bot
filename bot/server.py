"""Логика взаимодействия с телеграм-ботом"""

from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

bot = TelegramClient('bot', api_id, api_hash)

with bot:
    pass