# КОРТЕЖИ  (❗️❗️НЕИЗМЕНЯЕМЫЙ ТИП ДАННЫХ❗️❗️)
pets = ("Барсик", "Шарик", "Мурзик", "Белка")


t = (1, [2, 3], {"a": 123})
print(t)

t[2]["new"] = 123
print(t)

#
# pets = pets[1:]  # НЕ ИЗМЕНЕНИЕ!!!  (ПРИСВАИВАНИЕ)
#
#
# # МНОЖЕСТВА (SET)  ❗❗️️ПРИНИМАЮТ ТОЛЬКО НЕИЗМЕНЯЕМЫЕ ТИПЫ❗❗️️
# set1 = {1000, 2, "2", (2, 2), 3, 3, 4, 91, 123, 34}
#
# set1.add(1)
# set1.add(1)
#
#
# # ============= СЛОВАРЬ ===============
#
# person = {
#     # ключ: значение
#     "name": "Igor",
#     "age": 25,
# }
#
#
# person2 = {
#     # ключ: значение
#     "age": 25,
#     "name": "Max",
# }
#
#
# age = person["age"] / 23
# # age = 25 / 23
# print(age)
#
# text = person["name"] + ", hello"
# # text = 'Igor' + ', hello'
# print(text)
#
# names = [person["name"], person2["name"]]
# # names = ['Igor', 'Max']
# print(names)
#
#
# # `Обновление` значения ключа
# person["age"] = person["age"] + 1
# # person["age"] = 25 + 1
# # person["age"] = 26
# print(person["age"])
#
# # Добавление нового ключа
# person["address"] = "address string"
# print(person["address"])
#
# # Удаление ключа (его значения тоже)
# del person["address"]
# print(person["address"])  # ОШИБКА!!!
