def create_user(name: str, password: str, email: str, phone: str = ""):
    """
    Создает словарь пользователя, основываясь на переданных параметрах.
    """
    print("|def create_user|start")
    user = {
        "name": name,
        "password": password[::-1],
        "email": email,
        "phone": phone,
    }
    print("|def create_user|end")
    return user


def decorator_for_create_user(**kwargs) -> dict:
    print("|def user_decorator|Будет создан пользователь", kwargs["name"])
    user = create_user(**kwargs)
    print(f"|def user_decorator|Пользователь {user['name']} был успешно создан")
    return user


# print(create_user(name="Igor", password="pasdalsjk", email="mail@mail.com"))
user = decorator_for_create_user(
    name="Igor", password="pasdalsjk", email="mail@mail.com"
)

print(user)
