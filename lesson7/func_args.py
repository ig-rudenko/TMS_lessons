# Почему нет ограничения на кол-во параметров для `print` ?
print("asd", "asdasd", "asdas", "asdjih1209y1029312", 123, 123, 123)


# аргументы должны быть или `int`, или `float`.
# вернется или `int`, или `float` тоже.
def summ(*numbers: int | float) -> int | float:
    """
    Суммирует все переданные числа и возвращает сумму.
    """
    # `args` это кортеж всех аргументов, которые были переданы в функцию.
    total = 0
    for number in numbers:
        total += number
    return total


print(type(summ(1, 8, 0, 1)))
print(type(summ(1, 8.1, 0, 1)))
