# ************ Звездные выражение ***************

# ================  УПАКОВКА ===================

# Получение первого элемента из списка через распаковку

#           0        1         2        3
fio = ["Иванов", "Иван", "Иванович"]  # ...

surname = fio[0]  # Что это??
other_names = fio[1:]  # От 2го по счету элемента до конца
# print(surname, other_names)

# surname, first_name, last_name = fio  # 3 элемента
pets = ["Барсик", "Шарик", "Мурзик", "Белка"]

# p1, p2, p3, p4 = pets
# аналогично:
# p1, p2, p3, p4 = ["Барсик", "Шарик", "Мурзик", "Белка"]
# p1, p2, p3, p4 = "Барсик", "Шарик", "Мурзик", "Белка"

# первого в одну переменную, а все остальные в другую

p1, *other_pets = pets  # `*` это не умножение
# аналогично
# p1 = pets[0]
# other_pets = pets[1:]
print(p1, other_pets)
print(type(p1), type(other_pets))


first_pet, *other_pets, last_pet = pets  # `*` это не умножение
# аналогично
# first_pet = pets[0]
# last_pet = pets[-1]
# other_pets = pets[1:]
print(first_pet, other_pets, last_pet)
print(type(first_pet), type(other_pets), type(last_pet))


*other_pets, last_pet = pets  # `*` это не умножение
# аналогично
# last_pet = pets[-1]
# other_pets = pets[1:]
print(other_pets, last_pet)
print(type(other_pets), type(last_pet))


ids = [123, 124, 125, 126, 127, 128]  # ....

first_id, *_, last_id = ids  # `*` это не умножение
# аналогично
# first_pet = ids[0]
# last_pet = ids[-1]
print(first_id, last_id)
print(type(first_id), type(last_id))


# ==============  РАСПАКОВКА ===================
print("==============  РАСПАКОВКА ===================")

pets = ["Барсик", "Шарик", "Мурзик", "Белка"]

print(*pets)
