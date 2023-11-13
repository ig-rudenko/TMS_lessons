from .abstract import AbstractStorage


class InMemoryStorage(AbstractStorage):
    """
    Реализация абстрактного хранилища❗️
    Должен переопределить все абстрактные методы❗️
    """

    def __init__(self):
        self._storage: dict = {}

    def get(self, key: str):
        return self._storage.get(key)

    def set(self, key: str, value: str):
        self._storage[key] = value

    def delete(self, key: str):
        del self._storage[key]


class FileStorage(AbstractStorage):
    """
    Реализация абстрактного хранилища❗️
    Должен переопределить все абстрактные методы❗️
    """

    def __init__(self, filename: str):
        self._filename = filename

    def get(self, key: str):
        """
        Открываем файл, читаем построчно, и находим строку с ключом.
        """
        with open(self._filename, "r") as f:
            data = f.readlines()  # Создаем список строк
        for line in data:
            # разделяем строку 1 раз через символ `=` (слева)
            stored_key, value = line.split("=", 1)
            if stored_key == key:
                return value

    def set(self, key: str, value: str):
        with open(self._filename, "a") as f:
            # Символ переноса строки - `\n`
            f.write(f"{key}={value}\n")

    def delete(self, key: str):
        with open(self._filename, "r") as f:
            data = f.readlines()  # Создаем список строк

        i = 0
        deleted_index = -1
        while i < len(data):
            # разделяем строку 1 раз через символ `=` (слева)
            stored_key, value = data[i].split("=", 1)
            if stored_key == key:
                deleted_index = i
                break
        if deleted_index >= 0:
            data.pop(deleted_index)

        # Перезаписываем файл
        with open(self._filename, "w") as f:
            f.writelines(data)


class PersonStorage:
    def __init__(self, person: Person, storage: AbstractStorage):
        self._storage = storage
        self._person = person

    def save_user_data(self):
        self._storage.set("username", self._person.username)
        self._storage.set("password", self._person.password)
        self._storage.set("email", self._person.email)
