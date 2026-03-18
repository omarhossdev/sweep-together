import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_home_page(client: AsyncClient):
    response = await client.get("/")
    assert response.status_code == 200
    assert "HTMX" in response.text


@pytest.mark.asyncio
async def test_register_and_login(client: AsyncClient):
    # Register
    response = await client.post("/auth/register", data={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123",
    }, follow_redirects=False)
    assert response.status_code == 303

    # Login
    response = await client.post("/auth/login", data={
        "username": "testuser",
        "password": "password123",
    }, follow_redirects=False)
    assert response.status_code == 303


@pytest.mark.asyncio
async def test_login_invalid(client: AsyncClient):
    response = await client.post("/auth/login", data={
        "username": "nobody",
        "password": "wrong",
    })
    assert "Invalid credentials" in response.text
