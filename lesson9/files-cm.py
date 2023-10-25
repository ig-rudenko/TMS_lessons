# Открыть ТЕКСТОВЫЙ файл
# Контекстный менеджер


# UTF-16
# Отрываем файл, после выхода из блока, он сам закроется
# В качестве переменной открытого файла будет `file`
with open("text-utf-16", encoding="utf-16") as file:
    text_utf_16 = file.read()  # Читаем из файла

print(text_utf_16)

print("\n"*5)

# UTF-8
with open("text-utf-8", encoding="utf-8") as file:
    text_utf_8 = file.read()  # Читаем из файла
print(text_utf_8)

# Проверим наши строки

print(text_utf_16 == text_utf_8)

print("\n"*5)

# ASCII
with open("text-ascii", encoding="ascii", errors="replace") as file:
    text_ascii = file.read()  # Читаем из файла
print(text_ascii)

