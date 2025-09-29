from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from typing import Optional
from app.models.user import User

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_user_db = {
    "GID001": {
        "GID": "GID001",
        "name": "Test User",
        "email_id": "testuser@example.com",
        "hashed_password": pwd_context.hash("testpass")
    }
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(GID: str, password: str):
    user = fake_user_db.get(GID)
    if not user:
        return None
    if not verify_password(password, user["hashed_password"]):
        return None
    return User(GID=user["GID"], name=user["name"], email_id=user["email_id"], password="")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
