from fastadmin import WidgetType, register

from src.adapters.database.models import EmailTemplate
from src.adapters.database.repositories import EmailTemplateRepository
from src.admin.override_fastadmin import CustomModelAdmin
from src.schemas.admin.email_template import (
    EmailTemplateCreate,
    EmailTemplateGet,
    EmailTemplateList,
    EmailTemplateUpdate,
)


@register(EmailTemplate)
class EmailTemplateAdmin(CustomModelAdmin):
    EmailTemplate.__name__ = verbose_name = verbose_name_plural = "Шаблон писем"

    schemaCreate = EmailTemplateCreate
    schemaUpdate = EmailTemplateUpdate
    schemaGet = EmailTemplateGet
    schemaList = EmailTemplateList

    model_repository = EmailTemplateRepository

    list_display = ("type", "title")
    list_display_links = ("title",)
    list_filter = ("type", "title")

    search_fields = ("title",)

    fieldsets = ((None, {"fields": ("type", "title", "text")}),)

    formfield_overrides = {
        "type": (
            WidgetType.Select,
            {
                "required": True,
                "options": [
                    {"label": "запрос обратной связи", "value": 0},
                    {"label": "новый заказ", "value": 1},
                ],
            },
        ),
        "title": (WidgetType.Input, {"required": True}),
        "text": (WidgetType.TextArea, {"required": True}),
    }
