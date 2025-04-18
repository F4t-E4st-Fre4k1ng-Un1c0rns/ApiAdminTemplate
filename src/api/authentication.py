from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.schemas.api.authentication import (
    AuthenticationInput,
    AuthenticationOutput,
    RegistrationInput,
)
from src.service.authentication import AuthenticationService
from src.unit_of_work import UnitOfWork

authentication_router = APIRouter()


@authentication_router.post("/authentication", response_model=AuthenticationOutput)
async def authenticate(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)],
    credentials: AuthenticationInput,
):
    async with uow:
        return await AuthenticationService(uow).login(credentials)


@authentication_router.post("/registration", status_code=status.HTTP_201_CREATED)
async def register(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)],
    credentials: RegistrationInput,
):
    async with uow:
        await AuthenticationService(uow).register(credentials)

    return dict()
