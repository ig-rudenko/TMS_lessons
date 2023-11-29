from datetime import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship

# Строка подключения (DSN)

# Диалект - `sqlite`
# Обращение - `://`
# Путь - `/test.db` (В текущей папке)
dsn = "sqlite:///test.db"

# Точка входа в БД.
# `echo=True` - будут выводиться все действия с базой.
engine = create_engine(dsn, echo=True)

# Создаем новый класс для сессий, которые использует `engine`
# `autoflush=False` - убираем автоматическое подтверждение действий.
session = sessionmaker(bind=engine, autoflush=False)


# Создаем декларативную основу для будущих классов
class Base(DeclarativeBase):
    pass


# Создаем декларативное описание нашей таблицы
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    # nullable=False это NOT NULL
    username = Column(String(64), unique=True, nullable=False)
    password = Column(String(64), nullable=False)
    email = Column(String(200), unique=True, nullable=False)

    # Далее внутренние связи для SQLAlchemy
    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"User: {self.username}"


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(256))
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.now)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Далее внутренние связи для SQLAlchemy
    user = relationship("User", back_populates="posts")


def drop_tables():
    # Удаляем таблицы, которые унаследованы от `Base`
    Base.metadata.drop_all(engine)


def create_tables():
    # Создаем таблицы, которые унаследованы от `Base`
    Base.metadata.create_all(engine)


def add_users():
    with session() as connection:
        # Создали объект python. В базе его нет!
        user = User(username="igor", password="PASSWORD", email="igor@mail.com")

        # Добавим в таблицу запись через подключение
        connection.add(user)
        connection.add(
            User(username="user123", password="PASSWORD", email="user123@mail.com")
        )
        connection.add(
            User(username="user111", password="PASSWORD", email="user111@mail.com")
        )
        connection.add(
            User(username="user999", password="PASSWORD", email="user999@mail.com")
        )
        # Подтверждаем добавление!
        connection.commit()
