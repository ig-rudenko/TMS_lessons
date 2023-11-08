# Свой класс ошибок
class NANError(ArithmeticError):
    pass


class OutOfRangeError(ArithmeticError):
    pass


def to_float(value) -> float:
    try:
        # Снова пытаемся, но теперь во `float`
        valid_number = float(value)
    except ValueError:
        # Если выскочила ошибка `ValueError` мы её игнорируем, и делаем другой код.
        # Вызываем свою ошибку
        raise NANError(f"Переданное значение '{value}' не является числом")

    return valid_number


def validate_limit(number: float, limit: int) -> None:
    if number > limit:
        raise OutOfRangeError(
            f"Введенное число '{number}' вышло за допустимый предел '{limit}'"
        )


def main() -> None:
    while True:
        user_input: str = input("Введите число: ")

        try:
            # Мы пытаемся
            number = to_float(user_input)
            validate_limit(number, 1000)

        except (
            NANError,
            OutOfRangeError,
        ) as exc:  # Перехватываем ошибку, как экз. кл. ошибки
            print(exc)
        else:
            # В другом случае (если все же число)
            print("Ваше новое число:", number + 2)


try:
    main()
except KeyboardInterrupt:  # Перехватываем прерывание нашей программы
    print("\nСпасибо, до свидания!")
