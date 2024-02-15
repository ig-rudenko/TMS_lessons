import asyncio
import time


async def task1():
    print("Task 1 started")
    time.sleep(4)  # Блокирующий сон (имитируем CPU bound).
    print("Task 1 finished")


async def task2():
    print("Task 2 started")
    time.sleep(2)  # Блокирующий сон (имитируем CPU bound).
    print("Task 2 finished")


async def task3():
    print("Task 3 started")
    await asyncio.sleep(5)  # НЕ Блокирующий сон.
    print("Task 3 finished")


async def bad_task():
    print("bad_task started")
    while True:
        await asyncio.sleep(0.1)  # НЕ Блокирующий сон (имитируем CPU bound).
    print("bad_task finished")


async def main():
    start = time.perf_counter()
    tasks = [
        asyncio.create_task(bad_task()),
        asyncio.create_task(task3()),
        asyncio.create_task(task3()),
        asyncio.create_task(task3()),
    ]
    await asyncio.gather(*tasks)
    print("All tasks completed", round(time.perf_counter() - start, 2), "секунд")


asyncio.run(main())
