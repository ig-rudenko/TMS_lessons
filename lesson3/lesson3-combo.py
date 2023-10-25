person_igor = {
    # ключ: значение
    "name": "Igor",
    "age": 25,
}
person_max = {
    # ключ: значение
    "age": 23,
    "name": "Max",
}
person_mary = {
    # ключ: значение
    "age": 24,
    "name": "Mary",
}

# print(person_igor)

# Добавляем ему список по ключу "pets"
person_igor["pets"] = ["Барсик", "Шарик", "Мурзик", "Белка"]

# Добавляем список друзей
person_igor["friends"] = [person_max, person_mary]

print("Список друзей", person_igor["name"])
print(person_igor["friends"])

print("Лучший друг", person_igor["name"], "'s")
best_friend = person_igor["friends"][0]
# best_friend = person_igor["friends"][0]
# best_friend = [person_max, person_mary][0]
# best_friend = person_max
# best_friend = {'age': 23, 'name': 'Max'}

# best_friend - Это словарь

print("Его имя:", best_friend["name"])  # 'Max'
# best_friend - {'age': 23, 'name': 'Max'}
# best_friend["name"] - 'Max'

print()
print()

# =========== СПИСОК ЛЮДЕЙ НА ВЕЧЕРИНКУ =============
print("=========== СПИСОК ЛЮДЕЙ НА ВЕЧЕРИНКУ =============")

person_igor = {
    "name": "Igor",
    "age": 25,
}

person_max = {
    "age": 23,
    "name": "Max",
}
person_mary = {
    "age": 24,
    "name": "Mary",
}

# --------------  ЧЕРЕЗ СПИСОК  --------------------
print("--------------  ЧЕРЕЗ СПИСОК  --------------------")

persons_list = []
print(persons_list)

# Обращение к `МЕТОДУ` APPEND списка через ТОЧКУ `.`
# append - добавление элемента в конец списка
persons_list.append(person_igor)
persons_list.append(person_igor)
persons_list.append(person_igor)
persons_list.append(person_igor)
persons_list.append(person_max)
persons_list.append(person_mary)

print(persons_list)

persons_list = []  # Обнуление списка

print(persons_list)

# --------------  ЧЕРЕЗ МНОЖЕСТВО  --------------------
print("--------------  ЧЕРЕЗ МНОЖЕСТВО  --------------------")

persons_set = set()  # ❗️ПУСТОЕ МНОЖЕСТВО❗️

print(persons_set)

# Обращение к `МЕТОДУ` ADD множества через ТОЧКУ `.`
# append - добавление элемента в конец списка
person_igor_tuple = (person_igor["name"], person_igor["age"])
# person_igor_tuple = ('Igor', 25)
persons_set.add(person_igor_tuple)
persons_set.add(person_igor_tuple)
persons_set.add(person_igor_tuple)
persons_set.add(person_igor_tuple)

person_max_tuple = (person_max["name"], person_max["age"],)
persons_set.add(person_max_tuple)

print(persons_set)

# print(persons_set)


