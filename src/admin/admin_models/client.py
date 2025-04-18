from fastadmin import WidgetType, register

from src.adapters.database.models import Client
from src.adapters.database.repositories import ClientRepository
from src.admin.override_fastadmin import CustomModelAdmin
from src.schemas.admin.clients import (
    ClientsCreate,
    ClientsGet,
    ClientsList,
    ClientsUpdate,
)


@register(Client)
class ClientAdmin(CustomModelAdmin):
    Client.__name__ = verbose_name = verbose_name_plural = "Клиенты"

    schemaCreate = ClientsCreate
    schemaUpdate = ClientsUpdate
    schemaGet = ClientsGet
    schemaList = ClientsList

    model_repository = ClientRepository

    list_display = ("phone", "first_name", "second_name", "email", "organization_name")
    list_display_links = ("phone",)
    list_filter = ("phone", "first_name", "second_name", "email", "organization_name")

    search_fields = ("phone", "first_name", "second_name", "email", "organization_name")
    raw_id_fields = ("manager_id", "discount_group_id")

    readonly_fields = ("create_date", "modify_date")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    "create_date",
                    "modify_date",
                    "client_type",
                    "phone",
                    "password",
                    "manager",
                    "discount_group",
                    "first_name",
                    "second_name",
                    "email",
                    "city",
                    "address",
                    "organization_name",
                    "inn",
                )
            },
        ),
    )
    formfield_overrides = {
        "client_type": (
            WidgetType.Select,
            {
                "required": True,
                "options": [
                    {"label": "физическое лицо", "value": "individ"},
                    {"label": "юридическое лицо", "value": "legal entitie"},
                ],
            },
        ),
        "phone": (WidgetType.PhoneInput, {"required": True}),
        "password": (
            WidgetType.PasswordInput,
            {"passwordModalForm": True, "required": True},
        ),
        "discount_group": (
            WidgetType.AsyncSelect,
            {
                "required": False,
                "parentModel": "С Группы скидок",
                "idField": "id",
                "labelFields": ("__str__", "id"),
            },
        ),
        "first_name": (WidgetType.Input, {"required": False}),
        "second_name": (WidgetType.Input, {"required": False}),
        "email": (WidgetType.EmailInput, {"required": False}),
        "city": (WidgetType.Input, {"required": False}),
        "address": (WidgetType.Input, {"required": False}),
        "organization_name": (WidgetType.Input, {"required": False}),
        "inn": (WidgetType.Input, {"required": False}),
    }
