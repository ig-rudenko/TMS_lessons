name = input("Ваше имя: ")
age = int(input("Ваш возраст: "))


text = """
==================
  Ваш профиль:
  Имя: {}
  Возраст: {}
==================
"""

format_text = text.format(name, age)
print(format_text)

text = """
==================
  Ваш профиль:
  Имя: {1}
  Возраст: {0}
==================
"""

#                          0    1
format_text = text.format(age, name)
print(format_text)


text = "Привет, {2}"
print(text.format(name))
