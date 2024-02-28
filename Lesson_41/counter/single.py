import time

COUNT = 50_000_000


def countdown(n):
    while n > 0:
        n -= 1


start = time.perf_counter()
countdown(COUNT)
end = time.perf_counter()

print('Затраченное время -', round(end - start, 4), "сек.")
