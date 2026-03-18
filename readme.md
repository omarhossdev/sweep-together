# HTMX + FastAPI Starter

A modern hypermedia-driven web application starter built with **FastAPI**, **HTMX**, **Jinja2**, and **Tailwind CSS**. No JavaScript framework needed — just fast, server-rendered HTML with sprinkles of interactivity.

## ✨ Features

- ⚡ **FastAPI** backend with async support
- 🔄 **HTMX** for dynamic interactions without writing JavaScript
- 🎨 **Tailwind CSS** for utility-first styling
- 📝 **Jinja2** templates with partials/layout system
- 🗄️ **SQLModel** (SQLAlchemy + Pydantic) ORM
- 🔐 **Session-based authentication** with password hashing
- 📊 **CRUD example** — full todo app with inline editing
- 🧪 **Pytest** test setup with httpx async client
- 🐳 **Docker** ready
- ♻️ **Hot reload** in development

## 🚀 Quick Start

```bash
# Clone
git clone https://github.com/kszongic/htmx-fastapi-starter.git
cd htmx-fastapi-starter

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload --port 8000
```

Visit [http://localhost:8000](http://localhost:8000)

## 📁 Project Structure

```
├── app/
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Settings & configuration
│   ├── database.py          # Database setup (SQLite default)
│   ├── auth.py              # Authentication helpers
│   ├── models/
│   │   ├── user.py          # User model
│   │   └── todo.py          # Todo model (example CRUD)
│   ├── routers/
│   │   ├── pages.py         # Page routes (HTML responses)
│   │   ├── auth.py          # Auth routes (login/register/logout)
│   │   └── todos.py         # Todo HTMX endpoints
│   ├── templates/
│   │   ├── base.html        # Base layout
│   │   ├── index.html       # Home page
│   │   ├── login.html       # Login page
│   │   ├── register.html    # Register page
│   │   ├── dashboard.html   # Dashboard with todo app
│   │   └── partials/
│   │       ├── todo_item.html
│   │       ├── todo_list.html
│   │       ├── todo_edit.html
│   │       └── flash.html
│   └── static/
│       ├── css/
│       │   └── app.css      # Tailwind + custom styles
│       └── js/
│           └── app.js       # Minimal JS (HTMX config)
├── tests/
│   ├── conftest.py
│   └── test_todos.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── tailwind.config.js
└── .env.example
```

## 🔄 How HTMX Works Here

Instead of building a JSON API + SPA, this starter uses HTMX to:

1. **Swap HTML fragments** — Server returns rendered HTML, HTMX swaps it into the DOM
2. **Inline editing** — Click to edit a todo, submit saves and swaps back
3. **Delete with animation** — Remove items with CSS transitions
4. **Form validation** — Server-side validation, errors rendered as HTML partials
5. **Flash messages** — Toast notifications via HTMX out-of-band swaps

No build step for JS. No virtual DOM. Just HTML over the wire.

## 🎨 Tailwind CSS

Tailwind is included via CDN for simplicity. For production, install and build:

```bash
npm install -D tailwindcss
npx tailwindcss -i ./app/static/css/app.css -o ./app/static/css/output.css --watch
```

## 🐳 Docker

```bash
docker compose up --build
```

## 🧪 Testing

```bash
pytest tests/ -v
```

## 🔧 Configuration

Copy `.env.example` to `.env` and configure:

```
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///./app.db
DEBUG=true
```

## 📚 Resources

- [HTMX Docs](https://htmx.org/docs/)
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [SQLModel Docs](https://sqlmodel.tiangolo.com/)
- [Tailwind CSS](https://tailwindcss.com/)

## License

MIT License — see [LICENSE](LICENSE)
