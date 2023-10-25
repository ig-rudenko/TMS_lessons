# Преобразования типов

# Пауза, пока пользователь не нажмет `ENTER`
name = input("Введите ваше имя: ")   # Возвращает всегда строку❗️

# Пауза, пока пользователь не нажмет `ENTER`
age = input("Введите ваш возраст: ")   # Возвращает всегда строку❗️

print("Ваше имя:", name.title())
print("Ваш возраст:", age)

print(type(age))
valid_age = int(age)                              # Преобразование типа
print(type(valid_age))

print("Через 10 лет вам будет:", valid_age + 10, "лет")

total_name_letters = list(age)                     # Преобразование типа
# Если name = "Игорь"
# Каждая буква будет элементом
# ['И', 'г', 'о', 'р', 'ь']

name_letters = set(name.lower())                    # Преобразование типа
# Если name = "Александра"
# Каждая буква будет элементом
# ['И', 'г', 'о', 'р', 'ь']

name_dict = dict.fromkeys(name_letters, 0)          # Преобразование типа

print(str(name_dict))                               # Преобразование типа
# аналогично - print(name_dict)

print("Ваше имя имеет длину:", len(name))
print("Ваше имя состоит из следующих букв:", total_name_letters)
print("Ваше имя содержит буквы:", name_letters)
