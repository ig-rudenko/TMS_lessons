def calculate_positive_numbers(numbers):
    summ = 0
    for number in numbers:
        if number <= 0:
            # Пропускает завершение текущей итерации
            continue
        summ += number
    return summ  # Возврат


some_numbers = [5, 0, 16, 99, -18, 5, -55, 15, -6, 0, 20, 10, -3]
result = calculate_positive_numbers(some_numbers)
print(result)

some_numbers = [0, 0, 0, 0, 12, 1, 1]
result = calculate_positive_numbers(some_numbers)
print(result)

some_numbers = [-55, 15, -6, 0, 20, 10, -3]
result = calculate_positive_numbers(some_numbers)
print(result)
