# Добавление в конец
print("# Добавление в конец")
list1 = [1, 2]
print(list1)
result = list1.append(3)  # ❗️этот метод возвращает ничего (None)
print("result:", result)
print(list1)


# Кол-во совпадений
print("# Кол-во совпадений")
list2 = [1, 2, 1, 1, 4, 5, 6, 8, 3, 4, 5, 6, 1]

result = list2.count(1)
print(result)               # 4

print(list2.count(5))       # 2
print(list2.count("text"))  # 0

# Расширение списка
print("# Расширение списка")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)

tuple1 = (7, 8, 9)
list1.extend(tuple1)  # ❗️этот метод возвращает ничего (None)
print(list1)

# Вставка
print("# Вставка")
#        0  1  2
list1 = [1, 2, 3]
# Вставка значения "text" по индексу `2`
list1.insert(0, "text")  # ❗️этот метод возвращает ничего (None)
print(list1)  # [1, 2, 'text', 3]

# Удаление по значению
print("# Удаление по значению")
list1 = ["4", "1", "2", "3", "4"]
print(list1)
list1.remove("4")  # ❗️этот метод возвращает ничего (None)
print(list1)

# Удаление (и взятие) по индексу
print("# Удаление по индексу")
#         0    1    2    3
list1 = ["1", "2", "3", "4"]
print(list1)
element = list1.pop(1)  # По индексу
print("Был удален элемент:", element)
print(list1)

