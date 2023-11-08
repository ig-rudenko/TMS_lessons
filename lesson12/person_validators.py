class Person:
    def __init__(self, username: str, email: str, superuser: bool = False):
        self.username = username
        self.email = email
        self._superuser = superuser

    @property
    def superuser(self):
        return self._superuser

    @superuser.setter
    def superuser(self, value):
        self._superuser = bool(value)


class Teacher(Person):

    def __init__(self, username: str, email: str, graduate: bool = False, superuser: bool = False):
        super().__init__(username, email, superuser)
        self.graduate = graduate


class Admin(Person):

    def __init__(self, username: str, email: str):
        super().__init__(username, email, superuser=True)


class Validator:
    def __init__(self, person: Person):
        # Благодаря наследованию
        # person будет принимать на вход все экземпляры класса `Person`,
        # а также все дочерние экземпляры от класса `Person`❗️❗️❗️
        self._person = person

    def is_valid(self) -> bool:
        """Проверяем правильность данных у `Person`"""
        return self._validate_email() and self._validate_username()

    def _validate_username(self) -> bool:
        """Проверяем, что username состоит только из букв"""
        return self._person.username.isalpha()

    def _validate_email(self) -> bool:
        """В E-mail должна быть `@`"""
        return "@" in self._person.email


p = Person("John", "<EMAIL>")

t = Teacher("Igor", "<EMAIL>", graduate=True)

a = Admin("Mike", "<EMAIL>")

validator = Validator(a)

print(validator.is_valid())
