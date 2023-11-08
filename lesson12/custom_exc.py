# Свой класс ошибок
class NANError(ArithmeticError):
    pass


class OutOfRangeError(ArithmeticError):
    pass


def to_float(value):
    try:
        # Снова пытаемся, но теперь во `float`
        return float(value)
    except ValueError:
        # Если выскочила ошибка `ValueError` мы её игнорируем, и делаем другой код

        # Вызываем свою ошибку
        raise NANError(f"Переданное значение '{value}' не является числом")


def main():
    while True:
        user_input: str = input("Введите число: ")

        try:
            # Мы пытаемся
            number = to_float(user_input)
        except NANError:
            # Если это не число
            print("Вы ввели не число")
        except OutOfRangeError:
            print("Вы вышли за границы диапазона")
        else:
            # В другом случае (если все же число)
            print("Ваше новое число:", number + 2)


try:
    main()
except KeyboardInterrupt:  # Перехватываем прерывание нашей программы
    print("\nСпасибо, до свидания!")
