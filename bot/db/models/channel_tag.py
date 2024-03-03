from .base import Base
from .tag import Tag

from sqlalchemy import (
    Table,
    ForeignKey,
    Column
    )


channel_tag = Table(
    'channel_tag',
    Base.metadata,
    Column('channel_id', ForeignKey('channels.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True),
)