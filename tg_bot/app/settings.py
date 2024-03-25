import logging
import os

from aiogram import Bot, Dispatcher

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=os.environ['BOT_TOKEN'])
# Диспетчер
dp = Dispatcher()
