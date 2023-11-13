print("# ================ CUSTOM GENERATORS ==================")

# ГЕНЕРАТОРЫ содержат поведение (функционал),
# которое будет применяться для каждого элемента.
# Они не содержат в себе результирующие значения, он его высчитывает
# В момент использования через `next` или в цикле `for`

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# начальный объект - numbers
# проходи последовательность - for n in numbers
# поведение (условие) - if n % 2 == 0
# результат - n
number_generator = (n for n in numbers if n % 2 == 0)

# АНАЛОГ
# def get_custom_iterator(numbers):
#     new_numbers = []
#     for n in numbers:
#         if n % 2 == 0:
#             new_numbers.append(n)
#     return iter(new_numbers)

print(number_generator)

print(next(number_generator))
print(next(number_generator))
print(next(number_generator))


print("# ================= ГЕНЕРАТОР НА ОСНОВЕ ФУНКЦИЙ =================")


def get_custom_generator(num: list[int]):
    for n in num:
        print("смотрим цифру", n)
        if n % 2 == 0:
            yield n   # Возврат значения из функции-генератора и
            # постановка на `паузу` функции-генератора, до следующего её вызова
            # с сохранением состояния.
            print("После yield")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
generator = get_custom_generator(numbers)

for n in generator:
    print(n)
