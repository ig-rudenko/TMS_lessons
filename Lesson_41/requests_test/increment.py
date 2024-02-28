import threading
import time


class Counter:
    def __init__(self, start=0):
        self.value = start

    def increment(self):
        self.value = self.value + 1


def worker(counter: Counter):
    print("Start")
    for _ in range(1_000_000):
        counter.increment()
    print("End")


c = Counter(0)

threads = [
    threading.Thread(target=worker, args=(c,)) for i in range(3)
]

start = time.perf_counter()
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end = time.perf_counter()

print("Значение счетчика:", c.value, "выполнялось", round(end - start, 4), "сек.")
