from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr


class MeOutpput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    clientInfo: Optional["ClientInfo"]
    organizationInfo: Optional["OrganizationInfo"]
    managerInfo: Optional["ManagerInfo"]


class ClientInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    surname: Optional[str] = None
    phone: str
    email: Optional[EmailStr] = None
    city: Optional[str] = None
    address: Optional[str] = None


class ClientShortInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    surname: str
    phone: str
    email: Optional[EmailStr] = None


class OrganizationInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    inn: Optional[str] = None


class ManagerInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    surname: str
    phone: str
    email: str


class ClientInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    surname: Optional[str] = None
    phone: str
    email: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None


class OrganizationInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: Optional[str] = None
    inn: Optional[str] = None


class MeInput(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    clientInfo: "ClientInput"
    organizationInfo: Optional["OrganizationInput"] = None


class MeDatabaseFields(BaseModel):
    first_name: Optional[str] = None
    second_name: Optional[str] = None
    email: Optional[str] = None
    phone: str
    city: Optional[str] = None
    address: Optional[str] = None
    organization_name: Optional[str] = None
    inn: Optional[str] = None
