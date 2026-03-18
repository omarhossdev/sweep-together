from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.config import BASE_DIR
from app.auth import get_user_id_from_token

router = APIRouter()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@router.get("/")
async def index(request: Request):
    token = request.cookies.get("session")
    user_id = get_user_id_from_token(token) if token else None
    return templates.TemplateResponse("index.html", {
        "request": request,
        "logged_in": user_id is not None,
    })


@router.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


@router.get("/dashboard")
async def dashboard(request: Request):
    token = request.cookies.get("session")
    user_id = get_user_id_from_token(token) if token else None
    if not user_id:
        from fastapi.responses import RedirectResponse
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "user_id": user_id,
    })
