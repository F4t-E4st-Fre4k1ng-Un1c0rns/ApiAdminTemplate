from typing import Optional

from pydantic import BaseModel, Field

from src.adapters.database.models.email import EmailType


class EmailTemplateCreate(BaseModel):
    type: EmailType
    title: str = Field(..., max_length=255)
    text: str


class EmailTemplateUpdate(BaseModel):
    type: Optional[EmailType] = None
    title: Optional[str] = Field(None, max_length=255)
    text: Optional[str] = None


class EmailTemplateGet(BaseModel):
    id: int
    type: EmailType
    title: str
    text: str


class EmailTemplateList(BaseModel):
    id: int
    type: EmailType
    title: str
