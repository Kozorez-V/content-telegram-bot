from .base import Base

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Tag(Base):
    name: Mapped[str] = mapped_column(String(60), nullable=False)