text = input("Введите любой текст: ")


output = """
Пользователь:     user1230
Кол-во символов:  {0}
Заметка:
    "{1}"
"""

# Если нет текста, то выводим оповещение об ошибке
# Если длина текста больше 20 символов, то выводи только первые 10, а потом ...
# В ином случае выводим весь текст.

if not text:  # len(text) == 0
    print("Нет содержимого")

elif len(text) >= 100:
    print(f"Слишком большой текст ({len(text)}), укажите меньше 100")

elif len(text) > 20:
    format_text = text[:10] + "..."
    print(output.format(len(text), format_text))

else:
    print(output.format(len(text), text))

# После сравнения
