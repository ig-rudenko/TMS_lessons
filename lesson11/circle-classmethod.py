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

    @classmethod
    def from_diameter(cls, diameter: int | float):
        """
        Классовый метод принимает первым параметром Класс, из которого он был вызван!

        Создает новый экземпляр класса `cls` на основе переданного диаметра.
        :param diameter: Число
        :return: экземпляр класса `cls`
        """
        return cls(diameter / 2)

    @classmethod
    def from_area(cls, area: int | float):
        radius = (area / cls.PI) ** 0.5
        return cls(radius)


class CircleNew(Circle):

    def new_method(self):
        return 0


circle_new = CircleNew.from_diameter(123)

circle_new.new_method()

print(type(circle_new))
print(circle_new.radius)
print(circle_new.area)

circle = Circle.from_area(circle_new.area)

print(circle.radius, circle_new.radius)
