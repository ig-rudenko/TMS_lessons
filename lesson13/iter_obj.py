# ****************** ИТЕРИРУЕМЫЕ ОБЪЕКТЫ ********************
# Те, у которых есть реализованные магический метод `__iter__`.
# Тот который может быть итератором.

# которые можно пройти через цикл for

# Строка это итерируемый объект
for letter in "Python":
    print(letter)


# ❗️ЧИСЛА НЕ ИТЕРИРУЕМЫЕ❗️
# for i in 123:
#     print(i)
#
# for i in 1.123:
#     print(i)

# Список это итерируемый объект
for element in [1, 2, 3, 4, 5]:
    print(element)

# Кортеж это итерируемый объект
for element in (1, 2, 3, 4, 5):
    print(element)

# Словарь это итерируемый объект
person = {"name": "John", "age": 24}

for key, value in person.items():
    print(key, value)

# Множества это итерируемый объект
for i in {1, 2, 3, 4, 5}:
    print(i)


# =======================================================================
# Как устроены итерируемые объекты

numbers: list[str] = ["18", "12", "3", "4", "5"]

res = map(int, numbers)

first = next(res)  # 18
second = next(res)  # 12
third = next(res)  # 3
next(res)
next(res)
# next(res)  # Выходим за пределы списка `numbers` - StopIteration

print("first", first)
print("second", second)
print("third", third)


# КАК ЭТО РАБОТАЕТ В ЦИКЛЕ `FOR`

numbers2 = [1, 2, 3, 4, 5]
# Вход в `for`
# ==========================
# Внутренняя реализация
__iterator = iter(numbers2)
while True:
    try:
        element = next(__iterator)
    except StopIteration:
        break
    # =====================
    # тут можно использовать `n`

    print(element)

    # Переход на следующую итерацию
