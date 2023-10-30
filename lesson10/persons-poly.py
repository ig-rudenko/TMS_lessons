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

        self.age = age
        self.last_name = last_name
        self.surname = surname
        self.first_name = first_name
        self.email = email


class Student(Person):
    def get_lessons(self) -> list:
        return [
            "Лекция 1",
            "Лекция 6",
            "Лекция 3",
        ]


class Teacher(Person):
    def get_lessons(self) -> list:
        return [
            "Лекция 1",
            "Лекция 2",
            "Лекция 3",
            "Лекция 4",
        ]


student1 = Student("user198", "i4y572ny3ik")
student2 = Student("user123", "i4y572ny3ik")
student3 = Student("useri901", "i4y572ny3ik")

teacher1 = Teacher("t2114", "sasdasd")
teacher2 = Teacher("t414", "sasdasd")
teacher3 = Teacher("t714", "sasdasd")

# Список экземпляров классов `Student` и/или `Teacher`
members: list[Student | Teacher] = [
    student1,
    teacher1,
    student2,
    student3,
    teacher2,
    teacher3,
]


new_members_usernames = []
for member in members:
    # ПОЛИМОРФИЗМ
    if "Лекция 6" in member.get_lessons():
        new_members_usernames.append(member.username)

print(new_members_usernames)
