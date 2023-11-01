class Circle:
    PI = 3.14  # Глобальный атрибут

    def __init__(self, radius: int | float):
        # Создаем новый атрибут для экземпляра класса `Circle`
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    # Вычисляемый атрибут (уже не метод)
    @property
    def area(self) -> int | float:
        return self.PI * self.__radius**2

    def __add__(self, other) -> "Circle":
        """
        <<Магический метод>>
        Автоматически вызывается, когда происходит сложение с нами.
        :param other: Любой объект, который будет прибавляться к текущему экземпляру `Circle`.
        :return: Результат сложения - `Circle`
        """
        if isinstance(other, Circle):
            new_area = self.area + other.area
            radius = (new_area / self.PI) ** 0.5
            return Circle(radius)
        elif isinstance(other, (int, float)):
            self.__radius += other
            return self

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        """Вычитание"""
        if isinstance(other, Circle):
            new_area = self.area - other.area  # !!!!!!!!!!!!!!!
            radius = (new_area / self.PI) ** 0.5
            return Circle(radius)
        elif isinstance(other, (int, float)):
            self.__radius -= other
            return self

    def __rsub__(self, other):
        """Вычитание"""
        if isinstance(other, Circle):
            new_area = other.area - self.area  # !!!!!!!!!!!!!!!!
            radius = (new_area / self.PI) ** 0.5
            return Circle(radius)
        elif isinstance(other, (int, float)):
            self.__radius -= other
            return self

    def __bool__(self):
        """
        Вызывается, когда мы хотим преобразовать Circle в тип bool.
        Проверка существования круга.
        """
        return bool(self.__radius)

    def __len__(self) -> int:
        return int(self.PI * 2 * self.__radius)

    def __str__(self) -> str:
        """Человеко-читаемое строковое представление объекта"""
        return f"Circle: {self.__radius}"

    def __repr__(self):
        """
        `Техническое` внутреннее строковое представление объекта
        """
        return f"<Circle: radius={self.__radius}>"

    def __call__(self, *args, **kwargs):
        """Это функция"""
        print("Функция!!???", *args, **kwargs)


c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)
c1 = c1 + 1  # __add__
print(c1.radius)
c1 = c1 - 2  # __sub__
print(c1.radius)

print(len(c1))  # __len__

print(bool(c1))  # __bool__

print(c1)  # __str__

print([c1, c2])  # __repr__

c2 = Circle(10)

c1("hello")
