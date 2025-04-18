from enum import IntEnum

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseContent


class ContentType(IntEnum):
    document = 0
    image = 1

    def __str__(self):
        return f"{self.name}"


class NewsContent(BaseContent):
    __tablename__ = "newsContents"
    news_id: Mapped[int] = mapped_column(ForeignKey("news.id"))
    news = relationship("News", back_populates="contents", lazy="selectin")
