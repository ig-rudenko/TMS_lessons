# Тут хранится только одна переменная в оперативной памяти
i = 0
while i < 1000:
    i += 1
    print(i)


# Тут хранится ВЕСЬ список в оперативной памяти
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in list1:
    print(i)


# Оставим только те элементы, квадраты которых четные
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Это хранится в оперативке
list_s = list(map(lambda x: x**2, list2))  # Это хранится в оперативке
list_f = list(filter(lambda x: x % 2 == 0, list_s))  # Это хранится в оперативке
print(list_f)


# Через `FOR`
res = []
for n in list2:
    if n*n % 2 == 0:
        res.append(n)
print(res)

# Через iter
res = list(filter(lambda x: x*x % 2 == 0, list2))
print(res)
