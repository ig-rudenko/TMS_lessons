import random


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

        # Приватный атрибут
        # К нему необходимо обращаться только внутри данного и дочернего класса
        # Вне класс есть доступ, но этого быть не должно
        self._password = password

        # Защищенный атрибут
        # К нему можно обращаться только внутри данного класса
        self.__id = random.randint(1000, 9999)

        self.age = age
        self.last_name = last_name
        self.surname = surname
        self.first_name = first_name
        self.email = email

    def get_id(self):
        return self.__id

    def set_new_id(self, new_id: int):
        self.__id = new_id

    def get_full_name(self):
        return self.first_name + " " + self.surname + " " + self.last_name

    def encrypt_password(self):
        self._password = self._password[::-1] + self._get_secret_key()

    # Приватный метод!
    # К нему необходимо обращаться только внутри класса
    def _get_secret_key(self) -> str:
        return self.username + "ASDLJAKSDHHASD"

    def json(self) -> dict:
        """
        Возвращает структуру, которая будет легко сериализоваться JSON
        """
        return {
            "username": self.username,
            "password": self._password,
            "age": self.age,
            "last_name": self.last_name,
            "surname": self.surname,
            "first_name": self.first_name,
            "email": self.email,
        }


class Student(Person):  # Дочерний класс, а `Person` родительский класс
    def get_student_info(self):
        return {}

    def set_new_password(self, password: str) -> None:
        """
        Создаем новый пароль и шифруем его
        """
        self._password = password
        self.encrypt_password()

    def get_lessons(self) -> list:
        return [
            "Лекция 1",
            "Лекция 6",
            "Лекция 3",
        ]


class Teacher(Person):  # Дочерний класс, а `Person` родительский класс
    def get_teacher_info(self):
        return {}

    def get_lessons(self) -> list:
        return [
            "Лекция 1",
            "Лекция 2",
            "Лекция 3",
            "Лекция 4",
        ]


person1 = Person("igor", "<PASSWORD>")


student1 = Student("user198", "i4y572ny3ik")
teacher1 = Teacher("t114", "sasdasd")


print("первоначальный ID учителя", teacher1.get_id())

teacher1.set_new_id(1)  # Хотим указать новый ID
print("новый ID учителя", teacher1.get_id())

student1.set_new_password("1234567890")
print(student1.json())

