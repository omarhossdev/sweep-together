from passlib.context import CryptContext
from itsdangerous import URLSafeSerializer
from fastapi import Request, HTTPException
from app.config import SECRET_KEY

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
serializer = URLSafeSerializer(SECRET_KEY)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_session_token(user_id: int) -> str:
    return serializer.dumps({"user_id": user_id})


def get_user_id_from_token(token: str) -> int | None:
    try:
        data = serializer.loads(token)
        return data.get("user_id")
    except Exception:
        return None


async def get_current_user_id(request: Request) -> int:
    token = request.cookies.get("session")
    if not token:
        raise HTTPException(status_code=303, headers={"Location": "/login"})
    user_id = get_user_id_from_token(token)
    if not user_id:
        raise HTTPException(status_code=303, headers={"Location": "/login"})
    return user_id
