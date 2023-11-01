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

        # Атрибут
        self.full_name: str = f"{self.surname} {self.first_name} {self.last_name}"

    def encrypt_password(self) -> None:
        self.password = self.password[::-1]

    def json(self) -> dict:
        """
        Возвращает структуру, которая будет легко сериализоваться JSON
        """
        return {
            "username": self.username,
            "password": self.password,
            "age": self.age,
            "last_name": self.last_name,
            "surname": self.surname,
            "first_name": self.first_name,
            "email": self.email,
        }


person1 = Person("igor", "<PASSWORD>")

person2 = Person("user198", "i4y572ny3ik")


print(person1.password)

print("Я зашифрую свой пароль")

person1.encrypt_password()

print(person1.password)


print(person2.json())
