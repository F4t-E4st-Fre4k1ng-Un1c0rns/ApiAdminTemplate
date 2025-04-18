from sqlalchemy.ext.asyncio import AsyncSession

from src.adapters.database.repositories import (
    ClientRepository,
    EmailTemplateRepository,
    ManagerRepository,
    NewsContentRepository,
    NewsRepository,
)
from src.utils.repositories_gateway import RepositoriesGatewayProtocol


class RepositoriesGateway(RepositoriesGatewayProtocol):
    def __init__(self, session: AsyncSession):
        self.client = ClientRepository(session)
        self.manager = ManagerRepository(session)
        self.news = NewsRepository(session)
        self.news_content = NewsContentRepository(session)
        self.email_template = EmailTemplateRepository(session)
