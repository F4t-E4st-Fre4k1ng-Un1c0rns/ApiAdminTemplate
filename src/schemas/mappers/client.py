from src.adapters.database.models import Client
from src.adapters.database.models.managers import Manager
from src.schemas.api.client import (
    ClientInfo,
    ManagerInfo,
    MeDatabaseFields,
    MeInput,
    MeOutpput,
    OrganizationInfo,
    OrganizationInput,
)


def to_client_input_to_database_fields(
    raw_client_record: MeInput,
) -> MeDatabaseFields:
    if raw_client_record.organizationInfo is None:
        raw_client_record.organizationInfo = OrganizationInput()
    return MeDatabaseFields(
        first_name=raw_client_record.clientInfo.name,
        second_name=raw_client_record.clientInfo.surname,
        email=raw_client_record.clientInfo.email,
        phone=raw_client_record.clientInfo.phone,
        city=raw_client_record.clientInfo.city,
        address=raw_client_record.clientInfo.address,
        organization_name=raw_client_record.organizationInfo.name,
        inn=raw_client_record.organizationInfo.inn,
    )


def to_client_info(client_record: Client) -> ClientInfo:
    return ClientInfo(
        name=client_record.first_name,
        surname=client_record.second_name,
        phone=client_record.phone,
        email=client_record.email,
        city=client_record.city,
        address=client_record.address,
    )


def to_organization_info(client_record: Client) -> OrganizationInfo:
    return OrganizationInfo(name=client_record.organization_name, inn=client_record.inn)


def to_manager_info(manager_record: Manager) -> ManagerInfo:
    return ManagerInfo(
        name=manager_record.first_name,
        surname=manager_record.second_name,
        phone=manager_record.phone,
        email=manager_record.email,
    )


def to_client_profile(client_record: Client) -> MeOutpput:
    return MeOutpput(
        id=client_record.id,
        clientInfo=to_client_info(client_record),
        organizationInfo=to_organization_info(client_record),
        managerInfo=to_manager_info(client_record.manager),
    )
