from .base import Base
from ..models import *

from sqlalchemy import (
    Table,
    ForeignKey,
    Column
    )


channel_tag = Table(
    'channel_tag_association',
    Base.metadata,
    Column('channel_id', ForeignKey('channels.id'), primary_key=True, nullable=False, unique=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True, nullable=False, unique=True),
)