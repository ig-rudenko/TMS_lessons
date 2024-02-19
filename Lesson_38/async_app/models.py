from sqlalchemy import Column, Integer, String, Text

from .database.base import Base, Manager


class Post(Base, Manager):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100))
    content = Column(Text())

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Post: {self.title}>"
