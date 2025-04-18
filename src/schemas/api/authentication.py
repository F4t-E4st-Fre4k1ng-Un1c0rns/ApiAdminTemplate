from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from src.adapters.database.models.clients import ClientType


class Credentials(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    phoneNumber: str = Field(pattern=r"^7\d{10}$")
    password: str


class AuthenticationInput(Credentials): ...


class RegistrationInput(Credentials):
    clientType: ClientType


class AuthenticationOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    accessToken: str
    accessTokenExpirationTime: datetime
    clientName: str | None
    clientType: ClientType
