text = "Анаграмма — это слово, составленное из перестановки букв другого слова."

# Развернуть буквы в каждом слове, слова должны быть в том же порядке.


def split(s: str) -> str:
    words = s.split()
    new_words = []
    for w in words:
        new_words.append(w[::-1])
    return " ".join(new_words)


print(split(text))

print("# MAP")

# map применяет к каждому элементу последовательности применяет функцию
new_text = " ".join(map(lambda x: x[::-1], text.split()))

print(new_text)

print("-" * 30)

print(text.split())
print(
    list(  # Преобразуем результат в список
        map(lambda x: x[::-1], text.split())  # map разворачивает каждое слово в списке
    )
)


# Список строк в список чисел
print("# Список строк в список чисел")

numbers = ["1", "23", "14.43", "-234", "0", "-2.23", "4", "1"]


def to_int(enter: list[str]) -> list[float]:
    result = []
    for element in enter:
        result.append(float(element))
    return result


print(numbers)
print(to_int(numbers))

print("WITH MAP")

print(numbers)
print(list(map(float, numbers)))

# ТУТ НЕ СМОТРИМ!
# И вернуть только положительные

result = list(filter(lambda x: x > 0, map(float, numbers)))

print(result)

# И снова в строку

result = list(map(str, (filter(lambda x: x > 0, map(float, numbers)))))

print(result)
