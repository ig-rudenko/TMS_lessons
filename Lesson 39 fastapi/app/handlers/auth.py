from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRouter
from sqlalchemy.exc import NoResultFound

from app import models
from ..schemas.auth import User, UserCreate, TokenPair
from ..services.auth import create_jwt_token_pair, get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/users", response_model=User)
async def register_user(user: UserCreate):
    await models.User.create(username=user.username, password=user.password, email=user.email)
    return user


@router.post("/token", response_model=TokenPair)
async def create_jwt(user: UserCreate):
    try:
        user_model = await models.User.get_valid_user(user.username, user.password)
    except NoResultFound:
        raise HTTPException(status_code=400, detail="User not found")

    jwt_pair = create_jwt_token_pair(user_model.id)

    return TokenPair(access_token=jwt_pair[0], refresh_token=jwt_pair[1])


@router.get("/me", response_model=User)
def verify_jwt(user: models.User = Depends(get_current_user)):
    print(user)
    return user
