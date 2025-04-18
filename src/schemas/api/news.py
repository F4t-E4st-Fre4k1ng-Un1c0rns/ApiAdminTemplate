from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class NewsOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    items: list["NewsInfo"]
    page: int
    limit: int
    total: int


class NewsByIdOutput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    date: date
    text: str
    url: list[str]


class NewsInfo(BaseModel):
    id: int
    title: str
    shortText: str
    publishDate: date
    url: Optional[str]
