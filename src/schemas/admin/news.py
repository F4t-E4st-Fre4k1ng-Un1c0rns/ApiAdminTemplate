from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class NewsCreate(BaseModel):
    title: str = Field(..., max_length=50)
    text: str


class NewsUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=50)
    text: Optional[str] = None


class NewsGet(BaseModel):
    id: int
    title: str
    text: str
    publish_date: datetime


class NewsList(BaseModel):
    id: int
    title: str
    text: str
