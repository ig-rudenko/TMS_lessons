class Circle:
    PI = 3.14  # Глобальный атрибут

    def __init__(self, radius: int | float):
        # Создаем новый атрибут для экземпляра класса `Circle`
        self.__radius = radius

    @property
    def radius(self) -> int | float:
        """
        Геттер `Getter`
        Возвращает значение защищенного атрибута
        """
        return self.__radius

    @radius.setter
    def radius(self, radius: int | float):
        """
        `Setter`
        Будет сам вызываться в момент указания нового значения для атрибута `radius`.
        """
        if self._new_radius_is_valid(radius):
            self.__radius = radius

    @staticmethod
    def _new_radius_is_valid(radius: int | float) -> bool:
        """
        Статический метод превращает метод в обычную функцию!

        Его можно вызывать как из объекта класса Circle, так и напрямую от самого класса.

        Статический метод, который не обращается к атрибутам и методам своего класса.
        Method '_new_radius_is_valid' may be 'static'.
        """

        # Что тип radius это либо int, либо float и, если это так и он больше 0
        if isinstance(radius, (int, float)) and radius > 0:
            return True

        # Что тип radius это либо int, либо float и, если это так и он МЕНЬШЕ ИЛИ РАВЕН 0
        elif isinstance(radius, (int, float)) and radius <= 0:
            print("Радиус должен быть больше 0")
            return False

        # Что тип radius это НЕ int и НЕ float
        else:
            print(
                f"Для радиуса ожидается тип int или float, был передал {type(radius)}"
            )
            return False

    # Вычисляемый атрибут (уже не метод)
    @property
    def area(self) -> int | float:
        return self.PI * self.__radius**2

    # Вычисляемый атрибут (уже не метод)
    @property
    def circumference(self) -> int | float:
        return self.PI * 2 * self.__radius


c = Circle(10)

print(c.circumference)  # Теперь обращение без `()` Это уже атрибут!
print(c.area)  # Теперь обращение без `()` Это уже атрибут!

c.radius = 11  # setter - запись | Вызывается @radius.setter

print(c.circumference)
print(c.area)

print(c.radius)  # getter - чтение
