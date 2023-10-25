# ❗️❗️СТРОКА ЭТО НЕИЗМЕНЯЕМЫЙ ТИП❗️❗️

string = "❗️❗️СТРОКА это НЕИЗМЕНЯЕМЫЙ ТИП❗️❗️🤗"

# Кол-во совпадений ПОДСТРОКИ
print(string.count("Ы"))    # 1
print(string.count("S"))    # 0
print(string.count("❗️"))   # 4
print(string.count("ЭТО"))  # 1

# ВСЕ МЕТОДЫ НИЖЕ НЕ ВЛИЯЮТ НА ЗНАЧЕНИЕ `string`

print(string.lower())  # В нижний регистр
print(string.upper())  # В верхний регистр
print(string.title())  # Заглавными
print(string.capitalize())  # Первая буква заглавная


# Удаляет лишние пробелы (слева и справа)
print("# Удаляет лишние пробелы")
s = "   имя фамилия "
print("Без форматирования:", s)
formatted_s = s.strip()
print("После форматирования:", formatted_s)


# ---------- Разделяет строку на список подстрок -------------
#         ❗️❗️По умолчанию это символ пробела❗️❗️

print("# Разделяет строку на список подстрок")
print("Разделяет строку на список подстрок".split())
# ['Разделяет', 'строку', 'на', 'список', 'подстрок']

domains = "google.com,ya.ru,example.com"
print(domains.split(","))                # Возвращает список
# ['google.com', 'ya.ru', 'example.com']
print(domains[0])  # 'google.com'
print(domains[0].upper())  # GOOGLE.COM

domains = "google.com;ya.ru;example.com"
print(domains.split("-------"))          # Возвращает список
# ['google.com;ya.ru;example.com']


# ========== Собираем строку из списка ❗️СТРОК❗️=============

print("# Собираем строку из списка")

list1 = ['Разделяет', 'строку', 'на', 'список', 'подстрок']
origin = " ".join(list1)
print(origin)  # 'Разделяет строку на список подстрок'

list2 = ['google.com', 'ya.ru', 'example.com']
origin = ",".join(list2)
print(origin)  # 'google.com,ya.ru,example.com'

list3 = ['123']  # Один элемент списка
origin = ",".join(list3)
print(origin)  # '123' - НЕТ ОБЪЕДИНЕНИЯ
