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

    def check_email(self) -> bool:
        """
        email должен содержать символ `@`
        """
        return "@" in self.email

    def json(self) -> dict:
        """
        Возвращает структуру, которая будет легко сериализоваться JSON
        """
        return {
            "username": self.username,
            "password": self.password,
            "age": self.age,
            "lastName": self.last_name,
            "surname": self.surname,
            "firstName": self.first_name,
            "email": self.email,
        }


class Student(Person):
    def __init__(self, username: str, password: str, group: str = "1", *args, **kwargs):
        # Мы вызываем родительский `__init__`, для того, чтобы создать все атрибуты,
        # прописанные в `__init__` родительского класса `Person`

        # `super()` - это обращение к оригинальному родительскому классу
        # `super().__init__()` - вызывает `Person.__init__()`
        super().__init__(username, password, *args, **kwargs)

        # Добавляем новый атрибут класса Student
        self.group = group

    def check_email(self) -> bool:
        """
        Email должен содержать username студента
        """
        # Выполним проверку email от дочернего класса
        super_check = super().check_email()

        check = self.username in self.email

        return super_check and check

    def json(self) -> dict:
        # `super().json()` - это обращение к оригинальному родительскому методу json()
        person_json = super().json()
        person_json["group"] = self.group
        return person_json


person1 = Person("igor", "<PASSWORD>", email="mail@")

print(person1.check_email())

person2 = Student("user198", "i4y572ny3ik", "12", email="user198@email")

print(person2.check_email())
