from .base import Base

from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlaclhemy.types import BigInteger


def Channel(Base):
    channel_id: Mapped[BigInteger]
    username: Mapped[str]