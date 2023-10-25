def decorator(func):
    """
    Декоратор принимает любую функцию и возвращает декоратор для неё.

    :param func: (Функция), которую надо декорировать.
    :return: (Функция) Декоратор для переданной функции.
    """

    def wrapper(*args, **kwargs):
        print("|def decorator with wrapper|Вызвана функция с аргументами:", args,  kwargs)
        res = func(*args, **kwargs)
        print(f"|def decorator with wrapper|Результат функции: {res}")
        return res

    return wrapper


@decorator
def get_positive_numbers(numbers: list[int | float]) -> list[int | float]:
    new_numbers = []
    for number in numbers:
        if number > 0:
            new_numbers.append(number)
    return new_numbers


# @decorator означает, что будет подменена функция `get_positive_numbers` на `wrapper` из `decorator`

# def wrapper(*args, **kwargs):
#     print("|def decorator with wrapper|Вызвана функция с аргументами:", args,  kwargs)
#     res = get_positive_numbers(*args, **kwargs)
#     print(f"|def decorator with wrapper|Результат функции: {res}")
#     return res


numbers1 = [1, 23, 14.43, -234, 0, -2.23, 4, 1]


print(get_positive_numbers(numbers1))
