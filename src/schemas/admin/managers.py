from typing import Annotated, Optional

from pydantic import BaseModel, Field, PlainValidator

from src.adapters.database.models.managers import Role
from src.utils.password import hash_password


class ManagersCreate(BaseModel):
    role: Role
    first_name: str = Field(..., max_length=50)
    second_name: str = Field(..., max_length=50)

    phone: str = Field(..., max_length=11)
    email: str = Field(..., max_length=255)
    password: Annotated[str, PlainValidator(hash_password)]


class ManagersUpdate(BaseModel):
    role: Optional[Role] = None
    first_name: Optional[str] = Field(None, max_length=50)
    second_name: Optional[str] = Field(None, max_length=50)

    phone: Optional[str] = Field(None, max_length=11)
    email: Optional[str] = Field(None, max_length=255)
    # there's no password
    # because changing password is overrided fastadmin's password


class ManagersGet(BaseModel):
    id: int
    role: Role
    first_name: str
    second_name: str

    phone: str
    email: str
    password: str


class ManagersList(BaseModel):
    id: int
    phone: str
    first_name: str
    second_name: str
