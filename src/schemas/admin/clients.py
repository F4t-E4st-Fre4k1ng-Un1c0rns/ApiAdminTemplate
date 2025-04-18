from datetime import datetime
from enum import StrEnum
from typing import Annotated, Optional

from pydantic import BaseModel, Field, PlainValidator

from src.utils.password import hash_password

OptionalString = Annotated[
    Optional[str],
    PlainValidator(
        lambda v: (
            v
            if (v is not None and v.replace(" ", "") != "" and len(v) <= 255)
            else None
        )
    ),
]


class ClientType(StrEnum):
    individ = "individ"
    legal_entitie = "legal entitie"


class ClientsCreate(BaseModel):
    client_type: ClientType
    phone: str = Field(..., max_length=11)
    password: Annotated[str, PlainValidator(hash_password)]

    manager_id: int

    discount_group_id: int

    first_name: Optional[str] = Field(None, max_length=50)
    second_name: Optional[str] = Field(None, max_length=50)
    email: OptionalString = None

    city: Optional[str] = Field(None, max_length=50)
    address: Optional[str] = Field(None, max_length=255)

    organization_name: Optional[str] = Field(None, max_length=255)
    inn: Optional[str] = Field(None, max_length=10)


class ClientsUpdate(BaseModel):
    client_type: Optional[ClientType] = None
    phone: Optional[str] = Field(None, max_length=11)
    # there's no password
    # because changing password is overrided fastadmin's password

    manager_id: Optional[int] = None

    discount_group_id: Optional[int] = None

    first_name: Optional[str] = Field(None, max_length=50)
    second_name: Optional[str] = Field(None, max_length=50)
    email: OptionalString = None

    city: Optional[str] = Field(None, max_length=50)
    address: Optional[str] = Field(None, max_length=255)

    organization_name: Optional[str] = Field(None, max_length=255)
    inn: Optional[str] = Field(None, max_length=10)


class ClientsGet(BaseModel):
    create_date: datetime
    modify_date: datetime

    client_type: Optional[ClientType]
    phone: str
    password: str

    manager_id: Optional[int]

    discount_group_id: Optional[int]

    first_name: Optional[str]
    second_name: Optional[str]
    email: OptionalString

    city: Optional[str]
    address: Optional[str]

    organization_name: Optional[str]
    inn: Optional[str]


class ClientsList(BaseModel):
    id: int
    phone: str
    first_name: Optional[str]
    second_name: Optional[str]
    email: Optional[str]
