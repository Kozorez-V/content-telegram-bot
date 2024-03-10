from .base import Base

import datetime
from typing import List


from sqlalchemy import (
    Table,
    ForeignKey,
    Column,
    String
    )

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
    )

from sqlalchemy.types import BigInteger


class Channel(Base):
    channel_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    posts: Mapped[List['Post']] = relationship(back_populates='channel')
    tags: Mapped[List['Tag']] = relationship(secondary=channel_tag, back_populates='channels')


class Post(Base):
    date: Mapped[datetime.datetime] = mapped_column(nullable=False)
    views: Mapped[int] = mapped_column(nullable=True)
    replies: Mapped[int] = mapped_column(nullable=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey('channels.id'))
    channel: Mapped['Channel']= relationship(back_populates="posts")
    tags: Mapped[List['Tag']] = relationship(
        secondary=post_tag, back_populates="posts"
    )


class Tag(Base):
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    posts: Mapped[List['Post']] = relationship(
        secondary=post_tag, back_populates='tags'
    )
    channels: Mapped[List['Channel']] = relationship(
        secondary=channel_tag, back_populates='tags'
    )
    

post_tag = Table(
    'post_tag_association',
    Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True, nullable=False, unique=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True, nullable=False, unique=True),
)


channel_tag = Table(
    'channel_tag_association',
    Base.metadata,
    Column('channel_id', ForeignKey('channels.id'), primary_key=True, nullable=False, unique=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True, nullable=False, unique=True),
)