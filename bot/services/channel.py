"""Работа с каналами"""

from ..config import (
    client,
    session_factory as Session)

from db.models import *


async def get_channel_data(channel: str) -> dict:
    """Получаем данные о канале"""

    channel_data = await client.get_entity(channel)

    return {
        'id': channel_data.id,
        'username': channel_data.username
    }


async def add_channel_to_db(channel_data: dict) -> None:
    """Добавляем канал в базу данных"""

    if channel_data is not None:
        async with Session.begin() as session:
            channel = Channel(channel_id=channel_data['id'],
                              username=channel_data['username'])
            session.add(channel)