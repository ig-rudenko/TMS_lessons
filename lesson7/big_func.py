def all_in(numbers_list: list):
    """
    Функция принимает список чисел и возвращает список положительных чисел,
    кол-во нулей в списке, кол-во положительных числе и кол-во отрицательных.

    :param numbers_list: Список чисел
    :return: Кортеж
    """

    res_new_numbers = []
    res_count_zero = 0
    res_count_positive = 0
    res_count_negative = 0

    for number in numbers_list:
        if number > 0:
            res_new_numbers.append(number)
            res_count_positive += 1
        elif number == 0:
            res_count_zero += 1
        else:
            res_count_negative += 1

    # Вернется кортеж!!!! (потому что переменные указаны через запятую)
    return res_new_numbers, res_count_zero, res_count_positive, res_count_negative


numbers = [5, 0, 16, 99, -18, 5, -55, 15, -6, 0, 20, 10, -3]

res = all_in(numbers)

# (
#    [5, 16, 99, 5, 15, 20, 10],    new_numbers
#    2,                             count_zero
#    7,                             count_positive
#    4                              count_negative
# )

print(res)

new_numbers, count_zero, count_positive, count_negative = all_in(numbers)

print(new_numbers, count_zero, count_positive, count_negative)
