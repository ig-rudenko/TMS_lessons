import os
import time
from multiprocessing import Process
from threading import current_thread

COUNT = 100_000_000

a = 1


def countdown(n):
    global a
    # print("Start thread")
    a += 1
    print(current_thread().name, os.getpid())
    while n > 0:
        n -= 1


if __name__ == '__main__':

    print(f"MAIN PID {os.getpid()}")

    start = time.perf_counter()

    process1 = Process(target=countdown, args=(COUNT // 2,))
    process2 = Process(target=countdown, args=(COUNT // 2,))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print('Затраченное время -', round(time.perf_counter() - start, 4), "сек.")
    print("a =", a)
