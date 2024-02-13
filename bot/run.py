"""Запуск бота"""

from bot import bot
from client import client

if __name__ == "__main__":
    bot.run_until_disconnected()
    client.run_until_disconnected()