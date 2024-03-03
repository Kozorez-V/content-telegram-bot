from .base import Base
from .post_tag import post_tag

import datetime
from typing import List

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
    )

from sqlalchemy import ForeignKey


class Post(Base):
    date: Mapped[datetime.datetime] = mapped_column(nullable=False)
    views: Mapped[int] = mapped_column(nullable=True)
    replies: Mapped[int] = mapped_column(nullable=True)
    channel_id: Mapped[int] = mapped_column(ForeignKey('channels.id'))
    channel: Mapped['Channel']= relationship(back_populates="posts")
    tags: Mapped[List['Tag']] = relationship(
        secondary=post_tag, back_populates="posts"
    )