from .base import Base
from .post_tag import post_tag
from .channel_tag import channel_tag

from typing import List

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
    )

from sqlalchemy import String


class Tag(Base):
    name: Mapped[str] = mapped_column(String(60), nullable=False)
    posts: Mapped[List['Post']] = relationship(
        secondary=post_tag, back_populates='tags'
    )
    channels: Mapped[List['Channel']] = relationship(
        secondary=channel_tag, back_populates='tags'
    )