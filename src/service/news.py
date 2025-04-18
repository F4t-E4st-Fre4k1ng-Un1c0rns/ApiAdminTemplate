from fastapi.exceptions import RequestValidationError

from src.schemas.api.news import NewsByIdOutput, NewsOutput
from src.schemas.mappers import to_news_many_output, to_news_one_output
from src.unit_of_work import UnitOfWork


class NewsService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_by_id(self, id: int) -> NewsByIdOutput:
        news = await self.uow.repositories.news.find_one(id=id)

        return to_news_one_output(news_record=news)

    async def get_by_page(self, page: int, limit: int) -> NewsOutput:
        if (page is not None and page < 1) or (limit is not None and limit < 0):
            raise RequestValidationError([])

        news = await self.uow.repositories.news.select_with_pagination(
            page, limit, self.uow.repositories.news.model.publish_date
        )
        return to_news_many_output(
            news_records=news,
            page=page,
            limit=len(news),
            total=await self.uow.repositories.news.count_filtered(),
        )
