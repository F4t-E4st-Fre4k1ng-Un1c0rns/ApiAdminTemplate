from enum import IntEnum

from sqlalchemy import SMALLINT, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class EmailType(IntEnum):
    call_back_request = 0
    new_order = 1


class EmailTemplate(Base):
    __tablename__ = "emailTemplates"
    id: Mapped[int] = mapped_column(SMALLINT, primary_key=True)
    type: Mapped[EmailType] = mapped_column(SMALLINT, unique=True)
    title: Mapped[str] = mapped_column(String(255))
    text: Mapped[str] = mapped_column(String)

    def __str__(self):
        return f"{self.title} {self.type}"
