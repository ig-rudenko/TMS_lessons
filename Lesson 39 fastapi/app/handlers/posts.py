from fastapi import Depends, HTTPException
from sqlalchemy.exc import NoResultFound
from fastapi.routing import APIRouter

from app import models
from app.schemas.posts import Post
from app.services.auth import get_current_user

router = APIRouter(prefix="/posts", tags=["posts"])


@router.get("/", response_model=list[Post])
async def show_all_posts():
    """Возвращает список всех записей!"""
    posts = await models.Post.all()
    return posts


@router.post("/", response_model=Post)
async def create_post(post_data: Post, user: models.User = Depends(get_current_user)):
    post = await models.Post.create(title=post_data.title, content=post_data.content, user_id=user.id)
    return post


@router.get("/{post_id}", response_model=Post)
async def show_post(post_id: int):
    try:
        return await models.Post.get(post_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="Post not found")
