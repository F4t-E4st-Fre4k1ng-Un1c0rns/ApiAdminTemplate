from bs4 import BeautifulSoup

from src.adapters.database.models import News
from src.schemas.api.news import NewsByIdOutput, NewsInfo, NewsOutput
from src.utils.get_file_url import get_file_url


def _get_short_text(html):
    text = BeautifulSoup(html, "html.parser").get_text()
    length = 250
    if len(text) > length:
        text = text[:length] + "..."
    return text


def to_news_one_output(news_record: News) -> NewsByIdOutput:
    return NewsByIdOutput(
        title=news_record.title,
        date=news_record.publish_date.date(),
        text=news_record.text,
        url=[get_file_url(content.uri) for content in news_record.contents],
    )


def to_news_many_output(
    news_records: list[News], page: int, limit: int, total: int
) -> NewsOutput:
    return NewsOutput(
        items=[
            NewsInfo(
                id=news_record.id,
                title=news_record.title,
                publishDate=news_record.publish_date.date(),
                shortText=_get_short_text(news_record.text),
                url=(
                    get_file_url(news_record.contents[0].uri)
                    if news_record.contents
                    else None
                ),
            )
            for news_record in news_records
        ],
        page=page,
        limit=limit,
        total=total,
    )
