import asyncio
import time

import aiohttp
import requests


def sync_download(url: str, filename: str) -> None:
    r = requests.get(url, stream=True)
    if r.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(r.content)
    print("+", end="")


async def async_download(url: str, filename: str) -> tuple[str, bool]:
    task_name: str = asyncio.current_task().get_name()
    print(f"Сейчас начала выполняться задача: {task_name}")

    flag = False
    # Создаем сессию, через асинхронный контекстный менеджер.
    async with aiohttp.ClientSession() as session:
        # Делаем GET запрос (асинхронный).
        async with session.get(url) as response:
            if response.status == 200:
                # Записываем в файл (блокирующим вызовом).
                with open(filename, 'wb') as file:
                    # Дожидаемся получения данных.
                    data: bytes = await response.read()
                    file.write(data)
                    flag = True

    print("*", end="")  # Не будет переноса строки.
    return task_name, flag


async def main():
    files_count = 30
    image_url = "https://www.papiro-bookstore.com/wp-content/uploads/2021/12/Using-Asyncio-in-Python_-Understanding-Pythons-Asynchronous-Programming-Features.jpg"

    image_folder = "images"

    # ------------ ASYNC
    start = time.perf_counter()
    print("Async downloading images...")
    tasks: list[asyncio.Task] = []

    # Создали список задач (НЕ выполняя их).
    for i in range(files_count):
        tasks.append(
            asyncio.create_task(
                async_download(image_url, f"{image_folder}/async_image_{i}.png"),
                name=f"async_download-{i}"
            )
        )

    results = await asyncio.gather(*tasks)
    print(results)

    end = time.perf_counter()
    print("Async downloading time:", round(end - start, 4))

    # ----------- SYNC
    start = time.perf_counter()
    print("Common downloading images...")
    for i in range(files_count):
        sync_download(image_url, f"{image_folder}/sync_image_{i}.png")

    end = time.perf_counter()
    print("Common downloading time:", round(end - start, 2))


if __name__ == '__main__':
    asyncio.run(main())
