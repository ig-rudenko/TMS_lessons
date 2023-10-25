def create_user(username: str, password: str, age: int = -1, **kwargs):
    """
    Создает словарь пользователя, основываясь на переданных параметрах.
    Если не был передан параметр `is_superuser`, то по умолчанию будет `False`.

    Данная функция автоматически принимает бесконечное кол-во любых именованных аргументов.

    kwargs это словарь!

    Он принимает в себя ВСЕ именованные аргументы, которые НЕ указаны в функции.
    """

    print(f"ЧТО ТАКОЕ `kwargs` Тип: {type(kwargs)} Значение: {kwargs}")

    user = {
        "name": username,
        "age": age,
        "password": password,
    }
    user.update(kwargs)  # Добавляем в словарь новый словарь (расширение словаря)
    # P.S. Пример расширения словаря в конце файла

    return user


user1 = create_user(
    "user01282",
    "password1",
    25,
)

# Благодаря указанному в функции аргументу `**kwargs`
# помимо УКАЗАННЫХ аргументов: `username`, `password` и `age`
# можно передавать ЛЮБЫЕ ИМЕНОВАННЫЕ аргументы
user2 = create_user(
    "user17018",
    "password2",
    email="example@mail.com",
    phone="1i9239172837",
)
# Тут другие
user3 = create_user(
    username="user17018",
    password="password2",
    hobby="example@mail.com",
    is_superuser=True,
)

# Далее пользователи помимо обязательных ключей будут иметь уникальные
print(user1)
print(user2)
print(user3)


# Пример расширения словаря:

a = {
    "text": "привет!",
}
new_dict = {
    "pre_text": "=======",
    "post_text": "как дела?",
}

a.update(new_dict)

print(a)  # {'text': 'привет!', 'pre_text': '=======', 'post_text': 'как дела?'}
