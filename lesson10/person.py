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
        self.username = username
        self.password = password

        self.age = age
        self.last_name = last_name
        self.surname = surname
        self.first_name = first_name
        self.email = email

    def encrypt_password(self):
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
