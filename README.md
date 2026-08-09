# 🧹 SweepTogether

## ✨ Stack

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
git clone https://github.com/omarhossdev/sweep-together.git
cd sweep-together

#=================
# UV (Recommended)
#=================
# Install dependencies
uv sync

# Run for development
uv run uvicorn app.main:app --reload --port 8000

#=======================
# OR use pip
pip install -r requirements.txt
# Run 
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
├── pyproject.toml
└── .env.example
```

## License

MIT License — see [LICENSE](LICENSE)
