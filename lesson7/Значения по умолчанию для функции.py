# Значения по умолчанию для функций
def create_user(
    name: str, password: str, age: int, address: str, is_superuser: bool = False
):
    """
    Создает словарь пользователя, основываясь на переданных параметрах.
    Если не был передан параметр `is_superuser`, то по умолчанию будет `False`.
    """

    user = {
        "name": name,
        "age": age,
        "password": password,
        "address": address,
        "is_superuser": is_superuser,
    }
    return user


# Передача значений по имени аргумента
# Сначала идет позиционные аргументы, а потом именованные!
# У user1 значение `is_superuser` будет установлено по умолчанию `False` (как указано при объявлении функции)
user1 = create_user("igor", "asdasdasd", address="Earth", age=25)

# У user2 мы явно указали значение `is_superuser`
user2 = create_user("igor", "asdasdasd", address="Earth", age=25, is_superuser=True)
print(user1)

if user1["age"] >= 18:
    print("Можно купить")
else:
    print("Нельзя")


if user2["is_superuser"]:  # Тут вернется True или False
    print("У вас неограниченные права!")
else:
    print("Ваши права только на чтение :(")
