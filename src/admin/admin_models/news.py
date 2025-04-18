from datetime import datetime, timedelta

from fastadmin import WidgetType, register

from src.adapters.database.models import News
from src.adapters.database.repositories import NewsContentRepository, NewsRepository
from src.admin.override_fastadmin import (
    ContentParameter,
    CustomColumn,
    CustomModelAdmin,
)
from src.schemas.admin.news import NewsCreate, NewsGet, NewsList, NewsUpdate


@register(News)
class NewsAdmin(CustomModelAdmin):
    News.__name__ = verbose_name = verbose_name_plural = "Новости"

    schemaCreate = NewsCreate
    schemaUpdate = NewsUpdate
    schemaGet = NewsGet
    schemaList = NewsList

    content_parameters = [
        ContentParameter(
            content_repository=NewsContentRepository,
            relation_id_field_name="news_id",
        )
    ]

    model_repository = NewsRepository
    custom_columns = [
        CustomColumn(
            column_name="поиск по дате публикации",
            get_new_value=(lambda record: record.publish_date),
            filter={
                "gte": (
                    lambda value_gte: datetime.fromisoformat(value_gte)
                    <= News.publish_date
                ),
                "lte": (
                    lambda value_lte: (
                        datetime.fromisoformat(value_lte) + timedelta(days=1)
                        > News.publish_date
                    )
                ),
            },
            sort_field=News.publish_date,
            widget_type=WidgetType.RangePicker,
        )
    ]

    list_display = ("поиск по дате публикации", "title")
    list_display_links = ("title",)
    list_filter = ("поиск по дате публикации", "title")

    search_fields = ("title",)
    readonly_fields = ("publish_date",)

    fieldsets = ((None, {"fields": ("title", "text", "publish_date", "images")}),)

    formfield_overrides = {
        "title": (WidgetType.Input, {"required": True}),
        "text": (WidgetType.RichTextArea, {"required": True}),
        "images": (WidgetType.Upload, {"required": False, "multiple": True}),
    }
