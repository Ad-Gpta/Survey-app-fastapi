from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserLogin
from app.auth.auth import authenticate_user

router = APIRouter()

@router.post('/login')
def login(user: UserLogin):
    user_obj = authenticate_user(user.GID, user.password)
    if not user_obj:
        return 0
    return 1
