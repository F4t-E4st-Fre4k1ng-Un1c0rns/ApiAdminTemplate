from enum import StrEnum

from sqlalchemy import BIGINT, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import BaseWithTelemetryTimestamps
from .managers import Manager


class ClientType(StrEnum):
    individ = "individ"
    legal_entitie = "legal entitie"


class Client(BaseWithTelemetryTimestamps):
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(BIGINT, autoincrement=True, primary_key=True)

    client_type: Mapped[ClientType]
    phone: Mapped[str] = mapped_column(String(11), unique=True)
    password: Mapped[str] = mapped_column(String(60))

    manager_id: Mapped[int] = mapped_column(ForeignKey("managers.id"))
    manager: Mapped[Manager] = relationship(back_populates="clients", lazy="selectin")

    first_name: Mapped[str] = mapped_column(String(50), nullable=True)
    second_name: Mapped[str] = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=True)

    city: Mapped[str] = mapped_column(String(50), nullable=True)
    address: Mapped[str] = mapped_column(String(255), nullable=True)

    organization_name: Mapped[str] = mapped_column(String(255), nullable=True)
    inn: Mapped[str] = mapped_column(String(10), nullable=True)

    def __str__(self):
        return f"{self.phone} {self.second_name} {self.first_name}"
