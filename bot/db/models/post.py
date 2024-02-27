from .base import Base

import datetime

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship)

from sqlalchemy import ForeignKey


class Post(Base):
    date: Mapped[datetime.datetime] = mapped_column(nullable=False)
    views: Mapped[int] = mapped_column(nullable=True)
    replies: Mapped[int] = mapped_column(nullable=True)
    channel_id = Mapped[int] = mapped_column(ForeignKey('channels.id'))
    channel: Mapped['Channel']= relationship(back_populates="posts")