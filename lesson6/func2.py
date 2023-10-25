def get_positive_numbers(numbers_list: list):
    new_numbers = []
    for number in numbers_list:
        if number > 0:
            new_numbers.append(number)
    return new_numbers


def count_zero(numbers_list: list):
    count = 0
    for number in numbers_list:
        if number == 0:
            count += 1
    return count


def count_positive(numbers_list: list):
    count = 0
    for number in numbers_list:
        if number > 0:
            count += 1
    return count


def count_negative(numbers_list: list):
    count = 0
    for number in numbers_list:
        if number < 0:
            count += 1
    return count


# Вернуть список, в котором только положительные числа
numbers = [5, 0, 16, 99, -18, 5, -55, 15, -6, 0, 20, 10, -3]

positive = get_positive_numbers(numbers)  # Вернется список

positive_count = count_positive(positive)  # Вернется число

print(f"Только положительные элементы в списке: {positive}")
print(f"Оригинальная последовательность: {numbers}")
print(f"Длина последовательности: {len(numbers)}")
print(f"В последовательности {count_zero(numbers)} нулей")
print(f"В последовательности {count_positive(numbers)} пол. чисел")
print(f"В последовательности {count_negative(numbers)} отр. чисел")
