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
    # Отправка email.
    return user


def get_all_users() -> list[User]:
    with session() as conn:
        return conn.execute(select(User)).scalars().all()


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
