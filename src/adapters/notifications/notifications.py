from typing import Any

from src.unit_of_work import UnitOfWork

from .smtp import Client
from .templates import NotificationTextFactory


class NotificationsGateway:
    def __init__(
        self,
        uow: UnitOfWork,
    ) -> None:
        self._uow = uow
        self._email_client = Client()
        self._text_factory = NotificationTextFactory(uow)

    async def send_new_order_notification(
        self, manager_address: str, context: dict[str, Any]
    ):
        async with self._email_client:
            await self._email_client.send_message(
                recipient_adresses=[manager_address],
                subject=await self._text_factory.render_new_order_subject(context),
                html_content=await self._text_factory.render_new_order_content(context),
            )

    async def send_call_back_notification(
        self, manager_addressses: list[str], context: dict[str, Any]
    ):
        async with self._email_client:
            await self._email_client.send_message(
                recipient_adresses=manager_addressses,
                subject=await self._text_factory.render_call_back_subject(context),
                html_content=await self._text_factory.render_call_back_content(context),
            )
