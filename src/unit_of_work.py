from asyncio import shield

from src.adapters.database.repository_gateway import (
    RepositoriesGateway,
    RepositoriesGatewayProtocol,
)
from src.adapters.database.session import async_session_maker
from src.adapters.filestorage.repository import (
    FileStorageProtocol,
    FileStorageRepository,
)
from src.adapters.filestorage.session import s3_session_factory
from src.utils.unit_of_work import UnitOfWorkProtocol


class UnitOfWork(UnitOfWorkProtocol):
    file_storage: FileStorageProtocol
    repositories: RepositoriesGatewayProtocol

    def __init__(self):
        self.db_session_factory = async_session_maker
        self.s3_session_facotry = s3_session_factory

    async def __aenter__(self):
        self.db_session = self.db_session_factory()
        self.s3_session = self.s3_session_facotry()

        self.file_storage = FileStorageRepository(self.s3_session)
        self.repositories = RepositoriesGateway(self.db_session)

        return self

    async def __aexit__(self, *args):
        await self.rollback()
        await shield(self.db_session.close())

    async def commit(self):
        await self.db_session.commit()

    async def rollback(self):
        await self.db_session.rollback()
