from sqlalchemy import URL
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from app.core.config import settings


class DatabaseHelper:
    def __init__(
        self,
        url: URL,
    ):
        self.engine = create_async_engine(
            url,
            echo=True,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self):
        async with self.session_factory() as session:
            yield session


db_helper = DatabaseHelper(
    url=URL.create(
        "postgresql+asyncpg",
        settings.db.user,
        settings.db.password,
        settings.db.host,
        settings.db.port,
        settings.db.name,
    )
)
