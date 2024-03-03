from .base import Base
from .channel_tag import channel_tag

from typing import List, TYPE_CHECKING

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
    )

from sqlalchemy.types import BigInteger

if TYPE_CHECKING:
    from .tag import Tag
    from .post import Post


class Channel(Base):
    channel_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    username: Mapped[str] = mapped_column(nullable=True)
    posts: Mapped[List['Post']] = relationship(back_populates='channel')
    tags: Mapped[List['Tag']] = relationship(secondary=channel_tag, back_populates='channels')