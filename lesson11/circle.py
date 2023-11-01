class Circle:
    PI = 3.14  # Глобальный атрибут

    def __init__(self, radius: int | float):
        # Создаем новый атрибут для экземпляра класса `Circle`
        self.__radius = radius

    def area(self) -> int | float:
        return self.PI * self.__radius**2

    def circumference(self) -> int | float:
        return self.PI * 2 * self.__radius


c = Circle(10)

print(c.circumference())

print(c.circumference())
