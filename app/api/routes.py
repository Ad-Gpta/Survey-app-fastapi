from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserLogin, Token
from app.auth.auth import authenticate_user, create_access_token

router = APIRouter()

@router.post('/login', response_model=Token)
def login(user: UserLogin):
    user_obj = authenticate_user(user.GID, user.password)
    if not user_obj:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')
    access_token = create_access_token({
        "sub": user_obj.GID,
        "name": user_obj.name,
        "email_id": user_obj.email_id
    })
    return {"access_token": access_token, "token_type": "bearer"}
