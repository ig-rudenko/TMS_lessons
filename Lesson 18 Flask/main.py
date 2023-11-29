from flask import Flask, Response, request
from sqlalchemy import exc

from crud import get_user, create_user
from models import create_tables, drop_tables, add_users

# Создаем приложение Flask
app = Flask(__name__)

drop_tables()
create_tables()
add_users()  # Создаем тестовых пользователей


# Автоматически вызывается по HTTP запросу:
# method: `get`
# path: `/` - main page
@app.route("/", methods=["GET"])
def home_page_view():
    return "<h1>Hello, World!</h1>"  # HTML


# Автоматически вызывается по HTTP запросу:
# method: `get`
# path: `/register`
@app.route("/register", methods=["GET"])
def get_register_view():
    """Возвращаем форму для регистрации"""
    # Формируем строку в формате HTML, чтобы браузер отобразил поля для ввода.
    return (
        "<h1> Регистрация </h1>"
        '<form action="/register" method="post">'  # Форма для отправки данных через метод `POST`.
        #   `action="/register"` - это путь, куда будут отправлены данные.
        #   Поля для заполнения:
        #   Атрибут `name="username"` указывает название поля.
        '   <p> Username: <input type="text" name="username"> </p>'  # `type="text"` - это поле для текста
        '   <p> Password: <input type="password" name="password"> </p>'  # `type="password"` - это сокрытое поле для текста
        '   <p> Email: <input type="email" name="email"> </p>'  # `type="email"` - это поле для EMAIL
        '   <p> <input type="submit"> </p>'  # Кнопка подтверждения отправки формы - `type="submit"`
        '</form>'
    )


# Автоматически вызывается по HTTP запросу:
# method: `post`
# path: `/register`
@app.route("/register", methods=["POST"])
def register_user_view():
    """Обрабатываем форму регистрации"""
    # Смотрим данные формы, отправленной пользователем.
    user_data = request.form
    # user_data это не редактируемый словарь.

    try:
        user = create_user(
            username=user_data["username"],
            password=user_data["password"],
            email=user_data["email"]
        )
    except exc.IntegrityError:
        # Если пользователь с таким `username` или `email` уже существует.
        return f"""Пользователь с username: {user_data['username']}
         либо с email: {user_data['email']} уже существует"""

    return f"""
        <h1>Ваш пользователь успешно создан!</h1>
        <p>ID: {user.id}</p>
    """


# Автоматически вызывается по HTTP запросу:
# method: `get`
# path: `/<username>`
@app.route("/<username>", methods=["GET"])
def users_view(username: str):
    """Вернет данные пользователя, если такого не найдено, то отправит статус 404."""

    try:
        user = get_user(username)
    except exc.NoResultFound:
        # Если в базе нет пользователя с таким `username`.
        # Статус код ответа указываем `404`, что означает `not found`.
        return Response("User not found.", status=404)

    return f"""
        <h1>Вы зашли на страницу {username}</h1>
        <p>Email: {user.email}</p>
        <p>Password: {user.password}</p>
    """
