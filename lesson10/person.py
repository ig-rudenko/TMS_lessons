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

    @classmethod
    def create_from_string(cls, s: str):
        data = str(s).split("-")  # ["name", "password", "email"]
        if len(data) == 3:
            return cls(username=data[0], password=data[1], email=data[2])
        # Создаем ошибку
        print("Неверный формат!")


class Student(Person):
    def study(self) -> None:
        print("study")

# Метод create_from_string, который принимает один параметр: s, и создает и
# возвращает объект класса Person на основе строки s. Строка s должна иметь
# формат “name-password-email”, где name - имя, password - пароль и email - почта. Этот
# метод должен быть декорирован как classmethod


person1 = Person.create_from_string("name-password-email")

print(person1)

student1 = Student.create_from_string("name-password-email")

print(student1)

