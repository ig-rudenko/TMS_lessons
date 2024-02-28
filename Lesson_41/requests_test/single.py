import time

import requests


def requests_test():
    resp = requests.get('https://www.python.org/')
    print(resp.status_code)


start = time.perf_counter()
for i in range(10):
    requests_test()

end = time.perf_counter()
print("Времени прошло для single thread", round(end - start, 4), "сек.")
