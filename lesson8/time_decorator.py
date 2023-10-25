import time


def count_time(func):
    def wrapper(*wrapper_args, **wrapper_kwargs):
        time_start = time.perf_counter_ns()  # Сколько сейчас времени

        res = func(*wrapper_args, **wrapper_kwargs)

        time_end = time.perf_counter_ns()  # Сколько сейчас времени
        print("Функция выполнялась", time_end - time_start, "нс")
        return res

    return wrapper


@count_time
def get_positive_numbers(numbers: list[int | float]) -> list[int | float]:
    new_numbers = []
    for number in numbers:
        if number > 0:
            new_numbers.append(number)
    return new_numbers


@count_time
def get_zero_numbers(numbers: list[int | float]) -> list[int | float]:
    new_numbers = []
    for number in numbers:
        if number == 0:
            new_numbers.append(number)
    return new_numbers


numbers1 = [1, 23, 14.43, -234, 0, -2.23, 4, 1]

print(get_positive_numbers(numbers1))


# Теперь get_positive_numbers это
def get_positive_numbers(*args, **kwargs):
    time_start = time.perf_counter_ns()

    # Оригинальная функция
    # ====================
    def func(numbers: list[int | float]) -> list[int | float]:
        new_numbers = []
        for number in numbers:
            if number > 0:
                new_numbers.append(number)
        return new_numbers

    res = func(*args, **kwargs)
    # ====================

    time_end = time.perf_counter_ns()
    print("Функция выполнялась", time_end - time_start, "нс")
    return res
