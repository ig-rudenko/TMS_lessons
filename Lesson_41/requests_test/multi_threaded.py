import time
from threading import Thread

import requests


def requests_test(url):
    resp = requests.get(url)
    print(resp.status_code)


start = time.perf_counter()
threads = []
for i in range(10):
    threads.append(
        Thread(target=requests_test, args=('https://www.python.org/',))
    )

for thread in threads:
    # Запускаем все потоки.
    thread.start()

for thread in threads:
    # Ожидаем завершения всех потоков.
    thread.join()

end = time.perf_counter()
print("Времени прошло для single thread", round(end - start, 4), "сек.")
