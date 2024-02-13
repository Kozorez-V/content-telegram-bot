"""Загрузка переменных из окружения"""

from dotenv import load_dotenv
import os

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')