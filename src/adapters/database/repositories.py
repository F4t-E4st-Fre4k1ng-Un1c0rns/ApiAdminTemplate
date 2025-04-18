from sqlalchemy import asc, desc, select

from src.adapters.database.models.managers import Role
from src.utils.repository import (
    SQLAlchemyRepository,
    SQLALchemyUserRepository,
    _sentinel,
)

from .models import Client, EmailTemplate, Manager, News, NewsContent


class ClientRepository(SQLALchemyUserRepository):
    model = Client

    async def register(self, **data):
        if not data.get("manager_id"):
            data["manager_id"] = (
                await ManagerRepository(self.session).find_filtered(role=Role.admin)
            )[-1].id
        return await super().register(**data)


class ManagerRepository(SQLALchemyUserRepository):
    model = Manager


class NewsRepository(SQLAlchemyRepository):
    model = News

    async def select_with_pagination(
        self,
        page: int,
        limit: int,
        order_by=_sentinel,
        descending=True,
    ):
        offset = (page - 1) * limit
        stmt = select(self.model)

        if order_by is not _sentinel:
            stmt = (
                stmt.order_by(desc(order_by))
                if descending
                else stmt.order_by(asc(order_by))
            )

        stmt = stmt.offset(offset).limit(limit)
        res = await self.session.execute(stmt)
        return res.unique().scalars().fetchall()


class NewsContentRepository(SQLAlchemyRepository):
    model = NewsContent


class EmailTemplateRepository(SQLAlchemyRepository):
    model = EmailTemplate
