from dataclasses import dataclass, field


@dataclass  # Смотреть импорт
class Person:
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
