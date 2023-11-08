# =============== ИСКЛЮЧЕНИЯ ====================


user_input: str = input("Введите число: ")

# Мы проверяем все возможные варианты
# Если не проверить, то произойдет ошибка!
# ValueError: invalid literal for int() with base 10: 'user_input'

# ValueError это класс ошибки

m = 1
if user_input[0] == "-":
    user_input = user_input[1:]
    m = -1

if user_input.isdigit():  # '123'
    number = int(user_input)
    print(number * 2 * m)
elif user_input.count(".") == 1:
    other = user_input.replace(".", "")
    if other.isdigit():
        number = float(user_input)
        print(number * 2 * m)
    else:
        print("Это не число!")
else:
    print("Это не число!")


user_input: str = input("Введите число: ")

try:
    # В этом блоке мы пытаемся что-то сделать
    print(int(user_input) * 2)
except ValueError:
    # Если выскочила ошибка `ValueError` мы её игнорируем, и делаем другой код
    try:
        # Снова пытаемся, но теперь во `float`
        print(float(user_input) * 2)
    except ValueError:
        print("Это не число!")
