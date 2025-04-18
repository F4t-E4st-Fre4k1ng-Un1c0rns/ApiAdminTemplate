from typing import Annotated

from fastapi import APIRouter, Depends, status

from src.adapters.jwt_token import JwtToken
from src.schemas.api.client import MeInput, MeOutpput
from src.service.clients import ClientService
from src.unit_of_work import UnitOfWork
from src.utils.dependencies import provide_jwt_token

client_router = APIRouter()


@client_router.get("/me", response_model=MeOutpput)
async def get_current_client(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)],
    jwt_token: Annotated[JwtToken, Depends(provide_jwt_token)],
):
    async with uow:
        return await ClientService(uow).get_profile(client_id=jwt_token.client_id)


@client_router.put("/me", status_code=status.HTTP_200_OK)
async def put_me(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)],
    data: MeInput,
    jwt_token: Annotated[JwtToken, Depends(provide_jwt_token)],
):
    async with uow:
        await ClientService(uow).put_me(
            jwt_token.client_id, jwt_token.client_type, data
        )
    return dict()
