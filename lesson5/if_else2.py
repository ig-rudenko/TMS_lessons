n = int(input("Число: "))

# Если число больше 0, то прибавить к нему 100
# Если меньше - вычесть 100.

print("число больше 0?", n > 0)

# УСЛОВНЫЕ ОПЕРАТОРЫ

if n > 0:
    # True
    n = n + 100

elif n < 0:  # Иначе, если n меньше 0
    # True
    n = n - 100

else:
    # Иначе, когда n равно 0
    print("Ноль")

print("Ваше новое число: ", n)
