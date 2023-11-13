import os
import pathlib
# from pathlib import Path

print(os.name)  # ТИП ОС

print(os.sep)   # Какой символ используется для разделителя в пути

path = pathlib.Path()

# Создается генератор, для просмотра папки согласно паттерну
dir_glob = path.glob("*")

for file in dir_glob:
    print(file, file.is_dir(), file.absolute())

# Удалить, если нет файла, то ошибка
# file.unlink()
# Удалить, если нет файла, то НЕ будет ошибки
# file.unlink(missing_ok=True)


path = pathlib.Path("NEW_FILE")

if not path.exists():  # Если нет файла
    # path.touch()  # Создание пустого файла

    with path.open("w") as f:
        f.write("Hello World\n")

# Создает папку, если она есть, то НЕ будет ошибки
folder = pathlib.Path("NEW_FOLDER")
folder.mkdir(exist_ok=True)

# Создадим в папке файл
file = folder / "new_file.txt"
file2 = folder / "config.conf"
file3 = folder / "other" / "file.txt"

file.touch()
file2.write_text("server {}")  # Перезапись

# Создаем родительскую папку для файла
file3.parent.mkdir(exist_ok=True)

file3.touch()


# Посмотрим предков файла
p = pathlib.Path(r"E:\PycharmProjects\TMS_lesson2\lesson13\NEW_FOLDER")
print(p.parent)
print(p.parent.parent)
print(p.parent.parent.parent / "TMS_lesson2")
