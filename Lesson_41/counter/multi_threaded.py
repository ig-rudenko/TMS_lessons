import os
import time
from threading import Thread, current_thread

COUNT = 100_000_000


a = 1


def countdown(n):
    global a
    # print("Start thread")
    a += 1
    print(current_thread().name, os.getpid())
    while n > 0:
        n -= 1


t1 = Thread(target=countdown, kwargs={"n": COUNT // 2})
t2 = Thread(target=countdown, args=(COUNT // 2,))

print('ПРОЦЕСС С НОМЕРОМ', os.getpid())

start = time.perf_counter()

t1.start()
t2.start()

print("START ALL")

t1.join()  # Дожидаемся.
t2.join()  # Дожидаемся.

print('Затраченное время -', round(time.perf_counter() - start, 4), "сек.")
print("a =", a)
