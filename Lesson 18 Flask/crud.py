from sqlalchemy import select

from models import User, session


def get_user(username: str) -> User:
    with session() as conn:
        query = select(User).where(User.username == username)
        # (User,) - one()
        # User - scalar_one()
        return conn.execute(query).scalar_one()


def create_user(username: str, password: str, email: str) -> User:
    with session() as conn:
        user = User(username=username, password=password, email=email)
        conn.add(user)  # Добавляем.
        conn.commit()  # Подтверждаем создание.
        conn.refresh(user)  # Обновляем. Для чего? Получаем созданный ID из базы.
    return user
