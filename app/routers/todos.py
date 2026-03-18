from fastapi import APIRouter, Request, Depends, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.config import BASE_DIR
from app.database import get_session
from app.models.todo import Todo
from app.auth import get_current_user_id

router = APIRouter()
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@router.get("/")
async def list_todos(
    request: Request,
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_session),
):
    result = await session.exec(
        select(Todo).where(Todo.user_id == user_id).order_by(Todo.created_at.desc())
    )
    todos = result.all()
    return templates.TemplateResponse("partials/todo_list.html", {
        "request": request,
        "todos": todos,
    })


@router.post("/")
async def create_todo(
    request: Request,
    title: str = Form(...),
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_session),
):
    todo = Todo(title=title, user_id=user_id)
    session.add(todo)
    await session.commit()
    await session.refresh(todo)

    result = await session.exec(
        select(Todo).where(Todo.user_id == user_id).order_by(Todo.created_at.desc())
    )
    todos = result.all()
    return templates.TemplateResponse("partials/todo_list.html", {
        "request": request,
        "todos": todos,
    })


@router.put("/{todo_id}/toggle")
async def toggle_todo(
    request: Request,
    todo_id: int,
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_session),
):
    todo = await session.get(Todo, todo_id)
    if not todo or todo.user_id != user_id:
        return HTMLResponse("Not found", status_code=404)

    todo.completed = not todo.completed
    session.add(todo)
    await session.commit()
    await session.refresh(todo)
    return templates.TemplateResponse("partials/todo_item.html", {
        "request": request,
        "todo": todo,
    })


@router.get("/{todo_id}/edit")
async def edit_form(
    request: Request,
    todo_id: int,
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_session),
):
    todo = await session.get(Todo, todo_id)
    if not todo or todo.user_id != user_id:
        return HTMLResponse("Not found", status_code=404)
    return templates.TemplateResponse("partials/todo_edit.html", {
        "request": request,
        "todo": todo,
    })


@router.put("/{todo_id}")
async def update_todo(
    request: Request,
    todo_id: int,
    title: str = Form(...),
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_session),
):
    todo = await session.get(Todo, todo_id)
    if not todo or todo.user_id != user_id:
        return HTMLResponse("Not found", status_code=404)

    todo.title = title
    session.add(todo)
    await session.commit()
    await session.refresh(todo)
    return templates.TemplateResponse("partials/todo_item.html", {
        "request": request,
        "todo": todo,
    })


@router.delete("/{todo_id}")
async def delete_todo(
    todo_id: int,
    user_id: int = Depends(get_current_user_id),
    session: AsyncSession = Depends(get_session),
):
    todo = await session.get(Todo, todo_id)
    if not todo or todo.user_id != user_id:
        return HTMLResponse("Not found", status_code=404)

    await session.delete(todo)
    await session.commit()
    return HTMLResponse("")
