# Открыть ТЕКСТОВЫЙ файл
# Запись

# Создание нового файла
# Character Meaning
# 'r'  open for reading (default)
# 'w'  open for writing, truncating the file first
# 'x'  create a new file and open it for writing
# 'a'  open for writing, appending to the end of the file if it exists
# 'b'  binary mode
# 't'  text mode (default)
# '+'  open a disk file for updating (reading and writing)

# Открываем файл на перезапись (создаем если нет), кодировка utf-8
# with open("new_file", "w", encoding="utf-8") as new_file:
#     new_file.write(
#         """
# # Создание нового файла
# # Character Meaning
# # 'r'  open for reading (default)
# # 'w'  open for writing, truncating the file first
# # 'x'  create a new file and open it for writing
# # 'a'  open for writing, appending to the end of the file if it exists
# # 'b'  binary mode
# # 't'  text mode (default)
# # '+'  open a disk file for updating (reading and writing)
#         """
#     )


# Открываем файл на запись в конец, кодировка utf-8
with open("new_file", "w", encoding="utf-8") as new_file:
    # print(new_file.read())
    new_file.write(
        """
# Создание нового файла
# Character Meaning
# 'r'  open for reading (default)
# 'w'  open for writing, truncating the file first
# 'x'  create a new file and open it for writing
# 'a'  open for writing, appending to the end of the file if it exists
# 'b'  binary mode
# 't'  text mode (default)
# '+'  open a disk file for updating (reading and writing)
        """
    )


