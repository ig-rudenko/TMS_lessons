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


def create_product(id_: int, name: str, cost: float):
    """
    Создает словарь товар, основываясь на переданных параметрах.
    """
    print("|def create_product|start")
    product = {
        "id": id_,
        "name": name,
        "cost": cost,
    }
    print("|def create_product|end")
    return product


def decorator_for_create_user(**kwargs) -> dict:
    print("|def user_decorator|Будет создан пользователь", kwargs["name"])
    user = create_user(**kwargs)
    print(f"|def user_decorator|Пользователь {user['name']} был успешно создан")
    return user


def decorator_for_create_product(**kwargs) -> dict:
    print("|def product_decorator|Будет создан товар", kwargs["name"])
    user = create_product(**kwargs)
    print(f"|def product_decorator|Товар {user['name']} был успешно создан")
    return user


# print(decorator_for_create_product(id_=12312, name="phone", cost=1743))


def decorator_for_all(func, *args, **kwargs):
    """
    Декоратор принимает любую функцию и любые аргументы для неё.
    НЕ только именованные, а и любые позиционные!

    Выполняет код до вызова функции и после, затем возвращает результат.

    :param func: Функция
    :param kwargs: Именованные аргументы функции
    :return: Результат функции
    """
    print("|def decorator|Будет создан", kwargs)
    res = func(*args, **kwargs)
    print(f"|def decorator|{res} был успешно создан")
    return res

#
# print(
#     decorator_for_all(
#         func=create_user,  # Передаем название функции
#         name="Igor",
#         password="pasdalsjk",
#         email="mail@mail.com",
#     )
# )
#
# print(
#     decorator_for_all(
#         create_product,  # Передаем название функции
#         12312,
#         name="phone",
#         cost=1743,
#     )
# )

# Чтобы по имени create_user использовался вызов этой функций через декоратор для неё


def decorator(func):
    """
    Декоратор принимает любую функцию и возвращает декоратор для неё.

    :param func: (Функция), которую надо декорировать.
    :return: (Функция) Декоратор для переданной функции.
    """

    def wrapper(*args, **kwargs):
        print("|def decorator with wrapper|Будет создан", kwargs)
        res = func(*args, **kwargs)
        print(f"|def decorator with wrapper|{res} был успешно создан")
        return res

    return wrapper


create_user = decorator(create_user)


print(
    create_user("igor", password="password", email="mail@mail.com", phone=19286496234)
)
