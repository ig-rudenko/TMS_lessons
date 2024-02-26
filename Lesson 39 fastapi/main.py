from fastapi import FastAPI

from app.database.connector import db_conn
from app.handlers.auth import router as auth_router
from app.handlers.posts import router as posts_router

app = FastAPI()


@app.get("/status")
async def status():
    return {"status": "OK"}


@app.on_event("startup")
async def startup():
    db_conn.initialize("sqlite+aiosqlite:///db.sqlite3")


app.include_router(auth_router, prefix="/api")
app.include_router(posts_router, prefix="/api")
