import hashlib
import io
import os

import numpy as np
from redis import Redis
from PIL import Image, ImageDraw
from fastapi import FastAPI, Response

app = FastAPI()

# Подключение к Redis
redis_client = Redis.from_url(os.environ.get("REDIS_CACHE_URL", "redis://localhost:6379/0"))


def generate_avatar(avatar_size: int, nickname: str) -> bytes:
    background_color = '#f2f1f2'

    # Получаем набор псевдослучайных байт
    nic_bytes = hashlib.md5(nickname.encode('utf-8')).digest()

    # Получаем цвет из хеша
    main_color = nic_bytes[:3]
    # rgb
    main_color = tuple(channel // 2 + 128 for channel in main_color)

    # Генерируем матрицу заполнения блоков
    # массив 6 на 12
    need_color = np.array([bit == '1' for byte in nic_bytes[3:3 + 9] for bit in bin(byte)[2:].zfill(8)]).reshape(6, 12)
    # получаем матрицу 12 на 12
    need_color = np.concatenate((need_color, need_color[::-1]), axis=0)

    for i in range(12):
        need_color[0, i] = 0
        need_color[11, i] = 0
        need_color[i, 0] = 0
        need_color[i, 11] = 0

    # Рисуем изображения по матрице заполнения
    img_size = (avatar_size, avatar_size)
    block_size = avatar_size // 12  # размер квадрата
    print(block_size)

    img = Image.new('RGB', img_size, background_color)
    draw = ImageDraw.Draw(img)

    for x in range(avatar_size):
        for y in range(avatar_size):
            need_to_paint = need_color[x // block_size, y // block_size]
            if need_to_paint:
                draw.point((x, y), main_color)

    img_byte_array = io.BytesIO()
    img.save(img_byte_array, format='PNG')
    img_byte_array.seek(0)
    image_bytes = img_byte_array.getvalue()
    return image_bytes


def save_to_redis(username: str, image_data: bytes) -> None:
    redis_client.set(f"avatar-{username}", image_data)


@app.get("/avatar/")
def get_image(username: str):
    # Пытаемся получить изображение из кэша Redis
    cached_image = redis_client.get(username)
    if cached_image:
        return Response(content=cached_image, media_type="image/png")

    # Если изображение не найдено в кэше, генерируем новое
    avatar_image = generate_avatar(144, username)
    # Сохраняем в кэше Redis
    save_to_redis(username, avatar_image)

    return Response(content=avatar_image, media_type="image/png")
