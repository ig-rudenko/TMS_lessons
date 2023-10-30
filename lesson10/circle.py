# ООП - Объектно-ориентированное программирование

# Объекты это все что есть


class Circle:
    PI = 3.14  # Глобальный атрибут

    def __init__(self, radius: int | float):
        """
        `магический метод`

        Этот метод вызывается автоматически, при создании экземпляра класса `Circle`
        self это магия какая-то???

        :param radius: Тут понятно. Число.
        """

        # Создаем новый атрибут для экземпляра класса `Circle`
        self.radius = radius

    def area(self) -> int | float:
        # Глобальный атрибут PI
        # Обращение через `self.PI`

        return self.PI * self.radius**2

    def print(self):
        print("О")


c1 = Circle(1)
c2 = Circle(1283)

c3 = Circle(88.2423)


print(c3.area())
