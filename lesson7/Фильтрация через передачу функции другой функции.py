person1 = {
    "name": "Igor",
    "age": 24,
    "address": "Earth",
    "likesCount": 123123,
}
person2 = {
    "name": "Mike",
    "age": 25,
    "address": "Earth",
    "likesCount": 151572,
}
person3 = {
    "name": "Max",
    "age": 26,
    "address": "Earth",
    "likesCount": 24523,
}
person4 = {
    "name": "Anny",
    "age": 27,
    "address": "Earth",
    "likesCount": 65317,
}


def get_person_age(person: dict):
    return person["age"]


def get_person_name(person: dict):
    return person["name"]


def filter_persons_by_age(persons: list[dict]) -> list[dict]:
    """
    Функция принимает список людей и возвращает новый список в котором
    люди упорядочены по возрасту.

    :param persons: Список словарей с обязательным ключом `age`
    :return: Список словарей
    """

    # Встроенная функция sorted принимает в качестве
    # значения аргумента `key` другую функцию.

    # Она должна вернуть значение,
    # по которому будет осуществляться сортировка списка `person`.

    # В функцию `get_person_name` будет передаваться
    # все элементы по очереди из списка `person`.

    # ТУТ ПЕРЕДАЧА ФУНКЦИИ `get_person_name`, А НЕ ВЫЗОВ
    new_persons = sorted(persons, key=get_person_age)

    return new_persons


users_list = [person3, person1, person4, person2]

print(users_list)

print()


# def get_person_age(p):
#     return p["age"]

# Лямбда (анонимная функция)
# lambda p: p["age"]


print(sorted(users_list, key=get_person_age))


# Лямбда (анонимная функция)
# lambda p: p["age"]

print(sorted(users_list, key=lambda p: p["age"]))
