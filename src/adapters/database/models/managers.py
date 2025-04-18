from enum import IntEnum

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Role(IntEnum):
    manager = 0
    main_manager = 1
    admin = 2


class Manager(Base):
    __tablename__ = "managers"
    role: Mapped[Role]
    first_name: Mapped[str] = mapped_column(String(50))
    second_name: Mapped[str] = mapped_column(String(50))

    phone: Mapped[str] = mapped_column(String(11), unique=True)
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(60))

    clients = relationship("Client", back_populates="manager", lazy="selectin")

    def __str__(self):
        return f"{self.first_name} {self.second_name}"
