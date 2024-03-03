from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True
    __table_args__ = {'extend_existing': True}

    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'
    
    id: Mapped[int] = mapped_column(primary_key=True)