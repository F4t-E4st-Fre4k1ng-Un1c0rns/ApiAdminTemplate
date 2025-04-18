from typing import Annotated

from fastapi import APIRouter, Depends

from src.schemas.api.news import NewsByIdOutput, NewsOutput
from src.service.news import NewsService
from src.unit_of_work import UnitOfWork

news_router = APIRouter()


@news_router.get("/news", response_model=NewsOutput)
async def get_news(
    uow: Annotated[UnitOfWork, Depends(UnitOfWork)], page: int = 1, limit: int = 1
):
    async with uow:
        return await NewsService(uow).get_by_page(page=page, limit=limit)


@news_router.get("/news/{id}", response_model=NewsByIdOutput)
async def get_by_id(id: int, uow: Annotated[UnitOfWork, Depends(UnitOfWork)]):
    async with uow:
        return await NewsService(uow).get_by_id(id=id)
