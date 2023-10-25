# Открыть ТЕКСТОВЫЙ файл


# UTF-16
file = open("text-utf-16", encoding="utf-16")
text_utf_16 = file.read()  # Читаем из файла
file.close()  # Закрываем файл
print(text_utf_16)

print("\n"*5)

# UTF-8
file = open("text-utf-8", encoding="utf-8")
text_utf_8 = file.read()  # Читаем из файла
file.close()  # Закрываем файл
print(text_utf_8)

# Проверим наши строки

print(text_utf_16 == text_utf_8)

print("\n"*5)

# ASCII
file = open("text-ascii", encoding="ascii", errors="replace")
text_ascii = file.read()  # Читаем из файла
file.close()  # Закрываем файл
print(text_ascii)

