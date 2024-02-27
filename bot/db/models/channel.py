from .base import Base

from typing import List
from .post import Post

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship)

from sqlalchemy.types import BigInteger


class Channel(Base):
    channel_id: Mapped[BigInteger] = mapped_column(nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    posts: Mapped[List['Post']] = relationship(back_populate='channel')