"""Настройки проекта"""

import os
import logging
from dotenv import load_dotenv
from telethon.sync import TelegramClient

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker
    )

# Загрузка переменных из окружения

load_dotenv()

api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')
bot_token = os.getenv('BOT_TOKEN')

# Инициализация клиента

client = TelegramClient(
    'client',
    api_id,
    api_hash).start()

# Настройки базы данных

engine = create_async_engine(
    url=os.getenv('DB_URL'),
    echo=bool(os.getenv('DB_ECHO')),
    )

session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False
)

# Настройка логгирования

logging.basicConfig(filename="logs.log",
                    encoding='utf-8',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)