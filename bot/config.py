"""Настройки проекта"""

from dotenv import load_dotenv
import os
import logging

# Загрузка переменных из окружения

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

# Настройка логгирования

logging.basicConfig(filename="logs.log",
                    encoding='utf-8',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')