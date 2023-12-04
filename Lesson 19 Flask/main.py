from flask import Flask, Response, request, render_template, redirect, url_for
from sqlalchemy import exc

from crud import add_users, get_user, create_user, get_all_users
from models import create_tables, drop_tables

# Создаем приложение Flask
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/static-files/",  # Путь, по которому можно получить файлы их папки `static_folder`.
)

drop_tables()
create_tables()
add_users()  # Создаем тестовых пользователей


# Автоматически вызывается по HTTP запросу:
# method: `get`
# path: `/` - main page
@app.route("/", methods=["GET"])
def home_page_view():
    all_users = get_all_users()
    return render_template("home.html", users=all_users)  # HTML


# Автоматически вызывается по HTTP запросу:
# method: `get`
# path: `/register`
@app.route("/register", methods=["GET"])
def get_register_view():
    """Возвращаем форму для регистрации"""
    return render_template("register_form.html")


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

    # После успешного создания пользователя необходимо перенаправить на его страницу.
    return redirect(url_for("users_view", username=user.username))


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

    return render_template(
        "user.html",
        username=user.username,
        email=user.email,
        password=user.password
    )
