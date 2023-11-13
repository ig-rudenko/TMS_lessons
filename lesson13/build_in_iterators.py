print("# ================ RANGE =================")

for i in range(1, 10):
    print(i)

# Аналог
# i = 1
# while i < 10:
#     print(i)
#     i += 1

# С ШАГОМ
for i in range(1, 10, 2):
    print(i)


# Аналог
# i = 1
# while i < 10:
#     print(i)
#     i += 2


print("# ================ ENUMERATE =================")

word = "PYTHON"

for index, char in enumerate(word):
    print(f"Буква {char}, её индекс в слове {index}")
