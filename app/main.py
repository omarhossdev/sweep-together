from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.config import BASE_DIR, DEBUG
from app.database import init_db
from app.routers import pages, auth, events


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(title="Sweep Together", debug=DEBUG, lifespan=lifespan)

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

templates = Jinja2Templates(directory=BASE_DIR / "templates")

app.include_router(pages.router)
app.include_router(auth.router, prefix="/auth")
app.include_router(events.router, prefix="/events")
