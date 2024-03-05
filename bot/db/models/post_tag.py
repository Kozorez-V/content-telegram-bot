from .base import Base
from ..models import *

from sqlalchemy import (
    Table,
    ForeignKey,
    Column
    )


post_tag = Table(
    'post_tag_association',
    Base.metadata,
    Column('post_id', ForeignKey('posts.id'), primary_key=True, nullable=False, unique=True),
    Column('tag_id', ForeignKey('tags.id'), primary_key=True, nullable=False, unique=True),
)