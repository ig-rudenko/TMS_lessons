def full_file_opener(file_name):
    with open(file_name, "br") as f:
        data = f.read()  # Полное чтение файла
    return data


def file_generator(file, chunk_size: int):
    while True:
        data = file.read(chunk_size)  # Чтение файла по частям `1024` байта
        if not data:
            break
        yield data


# Через экранирование символа `\`
file_name1 = "C:\\Users\Igor\Downloads\\ubuntu-22.04.2-live-server-amd64.iso"
# Указать, что строка `raw` - буква `r` перед строкой
file_name2 = r"C:\Users\Igor\Downloads\ubuntu-22.04.2-live-server-amd64.iso"

with open(file_name1, "br") as f:
    gen = file_generator(f, 1024)
    for part in gen:
        print(len(part))


