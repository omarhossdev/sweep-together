from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.config import BASE_DIR
from app.database import get_session
from app.models.user import User
from app.auth import hash_password, verify_password, create_session_token

router = APIRouter()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@router.post("/register")
async def register(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    session: AsyncSession = Depends(get_session),
):
    existing = await session.exec(select(User).where(User.username == username))
    if existing.first():
        return HTMLResponse(
            '<div class="text-red-500 text-sm">Username already taken</div>',
            status_code=200,
        )

    user = User(username=username, email=email, hashed_password=hash_password(password))
    session.add(user)
    await session.commit()
    await session.refresh(user)

    response = RedirectResponse("/dashboard", status_code=303)
    response.set_cookie("session", create_session_token(user.id), httponly=True)
    return response


@router.post("/login")
async def login(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    session: AsyncSession = Depends(get_session),
):
    result = await session.exec(select(User).where(User.username == username))
    user = result.first()

    if not user or not verify_password(password, user.hashed_password):
        return HTMLResponse(
            '<div class="text-red-500 text-sm">Invalid credentials</div>',
            status_code=200,
        )

    response = RedirectResponse("/dashboard", status_code=303)
    response.set_cookie("session", create_session_token(user.id), httponly=True)
    return response


@router.get("/logout")
async def logout():
    response = RedirectResponse("/", status_code=303)
    response.delete_cookie("session")
    return response
