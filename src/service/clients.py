from src.adapters.database.models.clients import ClientType
from src.schemas.api.client import MeInput, MeOutpput
from src.schemas.mappers import to_client_input_to_database_fields, to_client_profile
from src.unit_of_work import UnitOfWork
from src.utils.exceptions import AccessDenied, UserNotRegistered


class ClientService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def get_profile(self, client_id) -> MeOutpput:
        if client_id == 0:  # Special case: unregistered user
            return MeOutpput(
                id=0,
                clientInfo=None,
                organizationInfo=None,
                managerInfo=None,
            )

        client = await self.uow.repositories.client.find_one(id=client_id)
        return to_client_profile(client_record=client)

    async def put_me(
        self, client_id: int, account_type: ClientType, profile_input: MeInput
    ):
        if client_id == 0:
            raise UserNotRegistered()
        if account_type == ClientType.individ and self._is_organization_info_changed(
            profile_input
        ):
            raise AccessDenied("Individuals cannot update organization info")
        await self.uow.repositories.client.edit_one(
            client_id,
            **to_client_input_to_database_fields(profile_input).model_dump(
                exclude_none=True
            ),
        )
        await self.uow.commit()

    def _is_organization_info_changed(self, profile_input):
        if profile_input.organizationInfo is not None:
            return False
        return (
            profile_input.organizationInfo.name is not None
            or profile_input.organizationInfo.inn is not None
        )
