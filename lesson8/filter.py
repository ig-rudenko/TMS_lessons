numbers1 = [1, 23, 14.43, -234, 0, -2.23, 4, 1]


def get_positive_numbers(numbers: list[int | float]) -> list[int | float]:
    new_numbers = []
    for number in numbers:
        if number > 0:
            new_numbers.append(number)
    return new_numbers


print(numbers1)
print(get_positive_numbers(numbers1))

# FILTER
print("# FILTER")


def is_positive(number: int | float) -> bool:
    return number > 0


print(numbers1)
new_numbers = list(filter(is_positive, numbers1))
print(new_numbers)


# FILTER + LAMBDA

print("# FILTER + LAMBDA")
print(numbers1)
new_numbers = list(filter(lambda x: x > 0, numbers1))
print(new_numbers)
