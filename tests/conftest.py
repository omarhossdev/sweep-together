import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlmodel import SQLModel
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import get_session

TEST_DB = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(TEST_DB)
test_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def override_get_session():
    async with test_session() as session:
        yield session


app.dependency_overrides[get_session] = override_get_session


@pytest_asyncio.fixture
async def client():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        yield ac
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
