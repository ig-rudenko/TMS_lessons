#          0         1         2        3
pets = ["Барсик", "Шарик", "Мурзик", "Белка"]

print("ЦИКЛ WHILE")

# === Заголовок
i = 0
while i < len(pets):
    pet = pets[i]
    # =====================

    print(pet)

    # =====================
    # Окончание
    i += 1  # i = i + 1

print("ЦИКЛ FOR")

# Проходит по очереди все элементы из списка
print("# Проходит по очереди все элементы из списка")
for pet in pets:
    # pet это произвольное название переменной
    # переменная `pet` в цикле for это аналог `pets[i]` из цикла while
    print(pet)

text = "hello, world!"
# Проходит по очереди все символы в строке
print("# Проходит по очереди все символы в строке")
for letter in text:
    # letter это произвольное название переменной
    print(letter)

numbers = {1, 3, 0, 4, 6}
# Проходит по очереди все элементы множества
print("# Проходит по очереди все элементы множества")
for number in numbers:
    # number это произвольное название переменной
    print(number)


# Проходит по очереди все ключи в словаре
person = {
    # ключ: значение
    "name": "Igor",
    "age": 25,
    "address": "text",
}
print("# Проходит по очереди все ключи в словаре")
# 'name', 'age', 'address'
for key in person:
    # key это произвольное название переменной
    print(key)

print("отображаем последовательность значений")
print(person.values(), type(person.values()))

# person.values()  -  dict_values(['Igor', 25, 'text'])  !!!это не список!!!
# Но его можно последовательно пройти
print("# Проходит по очереди все значения в словаре")
for value in person.values():
    # value это произвольное название переменной
    print(value)

print("отображаем последовательность ключей и значений")
print(person.items(), type(person.items()))
# person.items() -  dict_items([('name', 'Igor'), ('age', 25), ('address', 'text')])
# [
#   ('name', 'Igor'),
#   ('age', 25),
#   ('address', 'text')
# ]
print("# Проходит по очереди и ключи, и значения в словаре")
for key_value in person.items():
    # key_value = ('address', 'text')
    # key_value это произвольное название переменной
    print(f"Ключ: {key_value[0]}, Значение: {key_value[1]}")

print("# Проходит упрощенно по очереди и ключи, и значения в словаре")
for key_value in person.items():
    key, value = key_value  # ('name', 'Igor')
    # key 'name'
    # value 'Igor'

    # key_value это произвольное название переменной
    print(f"Ключ: {key}, Значение: {value}")

print("# Проходит БОЛЕЕ упрощенно по очереди и ключи, и значения в словаре")
for key, value in person.items():
    # key, value это произвольное название переменной
    print(f"Ключ: {key}, Значение: {value}")

