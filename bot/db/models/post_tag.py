from .base import Base

from sqlalchemy import (
    Table,
    ForeignKey,
    Column
    )


post_tag = Table(
    'post_tag',
    Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True),
)