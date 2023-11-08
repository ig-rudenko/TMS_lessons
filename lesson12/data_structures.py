import sys
from dataclasses import dataclass, field
from typing import TypedDict, NamedTuple


def get_person(name) -> dict:
    return {
        "username": name,
        "password": "data",
        "age": "data",
        "last_name": "data",
        "surname": "data",
        "first_name": "data",
        "email": "",
    }


# Мы не видим, откуда был получен и что из себя представляет person
person_dict = get_person("Igor")

print(person_dict["username"])  # Нет подсказки, какие есть ключи


# TypedDict


class PersonTypedDict(TypedDict):
    username: str
    password: str
    age: int
    last_name: str
    surname: str
    first_name: str
    email: str


def get_person(name) -> PersonTypedDict:
    return {
        "username": name,
        "password": "data",
        "age": 0,
        "last_name": "data",
        "surname": "data",
        "first_name": "data",
        "email": "",
    }


# Мы не видим, откуда был получен и что из себя представляет person
person_typed_dict = get_person("Igor")

print(person_typed_dict["password"])  # Есть подсказка, какие есть ключи!


# NamedTuple - именованный кортеж
# НЕЛЬЗЯ ИЗМЕНИТЬ ЗНАЧЕНИЯ ПОЛЕЙ ПОСЛЕ СОЗДАНИЯ ОБЪЕКТА

print("# NamedTuple - именованный кортеж")


class PersonNamedTuple(NamedTuple):
    username: str
    password: str
    age: int
    last_name: str = ""
    first_name: str = ""
    email: str = ""
    surname: str = ""


def get_person(name) -> PersonNamedTuple:
    return PersonNamedTuple(
        username=name,
        password="data",
        age=0,
    )


# Мы не видим, откуда был получен и что из себя представляет person
person_named_tuple = get_person("Igor")

print(
    person_named_tuple.username, person_named_tuple.password
)  # Это экземпляр класса PersonNamedTuple
# person.password = "<PASSWORD>"  # МЕНЯТЬ НЕЛЬЗЯ!


# dataclass - класс данных

print("# dataclass - именованный кортеж")


@dataclass  # Смотреть импорт
class PersonDataClass:
    username: str
    password: str
    age: int
    last_name: str = ""
    first_name: str = ""
    email: str = ""
    surname: str = ""
    # Список имен друзей, которые по умолчанию буду пустые
    friends: list[str] = field(default_factory=list)  # Смотреть импорт

    @property
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.surname} {self.last_name}"


def get_person(name) -> PersonDataClass:
    return PersonDataClass(
        username=name,
        password="data",
        age=0,
    )


# Мы не видим, откуда был получен и что из себя представляет person
person_dataclass = get_person("Igor")

print(
    person_dataclass.username, person_dataclass.password
)  # Это экземпляр класса PersonNamedTuple
person_dataclass.password = "<PASSWORD>"
print(person_dataclass.friends)


# Наш собственный класс


class Person:
    def __init__(
        self,
        username,
        password,
        email: str = "",
        age=None,
        first_name: str = "",
        surname: str = "",
        last_name: str = "",
    ):
        # Атрибуты
        self.username: str = username
        self.password: str = password

        self.age: int = age
        self.last_name: str = last_name.capitalize()
        self.surname: str = surname.capitalize()
        self.first_name: str = first_name.capitalize()
        self.email: str = email


person = Person(username="Igor", password="<PASSWORD>", age=22)


# Наш собственный класс с использованием `__slots__`


class PersonWithSlots:
    __slots__ = (
        "username",
        "password",
        "age",
        "email",
        "first_name",
        "surname",
        "last_name",
    )

    def __init__(
        self,
        username,
        password,
        email: str = "",
        age=None,
        first_name: str = "",
        surname: str = "",
        last_name: str = "",
    ):
        # Атрибуты
        self.username: str = username
        self.password: str = password

        self.age: int = age
        self.last_name: str = last_name.capitalize()
        self.surname: str = surname.capitalize()
        self.first_name: str = first_name.capitalize()
        self.email: str = email


person_with_slots = PersonWithSlots(username="Igor", password="<PASSWORD>", age=22)


# ================= РАЗМЕРЫ ОБЪЕКТОВ ======================

# 48 байт
print(f"dataclass занимает {sys.getsizeof(person_dataclass)} байт")

# 48 байт
print(f"class Person занимает {sys.getsizeof(person)} байт")

# 88
print(f"class PersonWithSlots занимает {sys.getsizeof(person_with_slots)} байт")

# 96 байт
print(f"NamedTuple занимает {sys.getsizeof(person_named_tuple)} байт")

# 360 байт
print(f"Словарь занимает {sys.getsizeof(person_dict)} байт")
# 360 байт
print(f"TypedDict занимает {sys.getsizeof(person_typed_dict)} байт")
