import pathlib

# Открываем в бинарном формате файл (ЛЮБОЙ)
# Размер файла
print(pathlib.Path("img.png").stat().st_size)

# Бинарный на чтение (НЕТ КОДИРОВКИ)
with open("img.png", "br") as file:
    image = file.read()
    # Перевели байты в hex (16-ая сист. исч.)
    print("Количество байт в картинке", len(image.hex()) // 2)


new_bytes = b"Python\x00"
print(new_bytes)

# Символ сердечка

h = "♥♦♣♠"
bytes_h = h.encode(encoding="utf-8")

print("♥ В байтах -", bytes_h)
print("♥ В 16ричной (hex) -", bytes_h.hex())
