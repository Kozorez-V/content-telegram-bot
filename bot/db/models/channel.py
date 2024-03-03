from .base import Base

from typing import List

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
    tags: Mapped[List['Tag']] = relationship(back_populates='channels')