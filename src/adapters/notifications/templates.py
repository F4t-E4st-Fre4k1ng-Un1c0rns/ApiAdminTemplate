from typing import Any

from jinja2 import BaseLoader, Environment

from src.adapters.database.models.email import EmailType
from src.unit_of_work import UnitOfWork


class NotificationTextFactory:
    def __init__(self, uow: UnitOfWork) -> None:
        self._jinja_env = Environment(loader=BaseLoader())
        self._uow = uow

    async def render_call_back_subject(self, context: dict[str, Any]):
        template_model = await self._uow.repositories.email_template.find_one(
            type=EmailType.call_back_request
        )
        template_jinja = self._jinja_env.from_string(template_model.title)
        return template_jinja.render(context)

    async def render_call_back_content(self, context: dict[str, Any]):
        template_model = await self._uow.repositories.email_template.find_one(
            type=EmailType.call_back_request
        )
        template_jinja = self._jinja_env.from_string(template_model.text)
        return template_jinja.render(context)

    async def render_new_order_subject(self, context: dict[str, Any]):
        template_model = await self._uow.repositories.email_template.find_one(
            type=EmailType.new_order
        )
        template_jinja = self._jinja_env.from_string(template_model.title)
        return template_jinja.render(context)

    async def render_new_order_content(self, context: dict[str, Any]):
        template_model = await self._uow.repositories.email_template.find_one(
            type=EmailType.new_order
        )
        template_jinja = self._jinja_env.from_string(template_model.text)
        return template_jinja.render(context)
