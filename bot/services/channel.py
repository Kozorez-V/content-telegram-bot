"""Работа с каналами"""

from config import (
    client,
    session_factory as Session)

from sqlalchemy import delete

from db.models import *

import logging


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

async def delete_channel_from_db(channel_data: dict) -> None:
    """Удаляем канал из базы данных"""

    channel_id = channel_data['id']

    async with Session.begin() as session:
        await session.execute(delete(Channel).where(Channel.channel_id == channel_id))
        logging.info(f'Канал {channel_id} удален успешно')