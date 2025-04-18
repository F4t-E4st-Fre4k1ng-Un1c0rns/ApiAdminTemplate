from datetime import datetime

from sqlalchemy import BIGINT, TIMESTAMP, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.utils.time import utc_signed_now

from .base import Base
from .contents import NewsContent


class News(Base):
    __tablename__ = "news"
    id: Mapped[int] = mapped_column(BIGINT, primary_key=True)

    title: Mapped[str] = mapped_column(String(50))
    text: Mapped[str]

    publish_date: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), default=utc_signed_now
    )

    contents: Mapped[list[NewsContent]] = relationship(
        back_populates="news", lazy="selectin", cascade="all, delete-orphan"
    )

    images: Mapped[list[str]] = mapped_column(ARRAY(String), nullable=True)

    def __str__(self):
        return f"{self.title}"
