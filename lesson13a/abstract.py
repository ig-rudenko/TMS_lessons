from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    """
    Абстрактный класс для хранилища значений переменных

    Абстрактный класс не должен иметь возможность создавать экземпляры

    Представляет общую структуру хранилища
    """

    @abstractmethod
    def get(self, key: str):
        """
        Позволяет получить по ключу какое-то значение.
        """

    @abstractmethod
    def set(self, key: str, value):
        """
        Позволяет записать по ключу какое-то значение.
        """

    @abstractmethod
    def delete(self, key: str):
        """
        Позволяет удалить по ключу какое-то значение.
        """
