from datetime import datetime, timedelta, timezone

from pydantic import BaseModel

from src.adapters.jwt_token import JwtToken
from src.schemas.api.authentication import (
    AuthenticationInput,
    AuthenticationOutput,
    RegistrationInput,
)
from src.schemas.mappers import (
    to_authentication_output,
    to_registration_database_fields,
)
from src.settings import settings
from src.unit_of_work import UnitOfWork
from src.utils.exceptions import ResultNotFound, UserAlreadyExist, WrongCredentials


class RegistrationData(BaseModel):
    client_info: RegistrationInput
    timestamp: datetime
    verification_code: int


class AuthenticationService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def login(self, credentials: AuthenticationInput) -> AuthenticationOutput:
        client = await self.uow.repositories.client.authenticate(
            phone=credentials.phoneNumber, password=credentials.password
        )

        if client.id == 0:
            raise WrongCredentials

        return to_authentication_output(
            client_record=client,
            access_token=JwtToken(
                exp=datetime.now(tz=timezone.utc)
                + timedelta(minutes=settings.JWT_TOKEN_LIFETIME),
                client_id=client.id,
                client_type=client.client_type,
            ),
        )

    async def register(self, credentials: RegistrationInput) -> None:
        try:
            await self.uow.repositories.client.find_one(phone=credentials.phoneNumber)
            raise UserAlreadyExist("User with this phone number already exist")
        except ResultNotFound:
            pass

        await self.uow.repositories.client.register(
            **to_registration_database_fields(credentials)
        )
        await self.uow.commit()
