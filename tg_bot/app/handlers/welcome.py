from aiogram import Router, types
from aiogram.filters.command import Command

router = Router()


@router.message(Command("start"))
async def home(message: types.Message):
    print("Пользователь", message.from_user.id, "отправил сообщение", message.text)
    await message.answer(
        "Привет😁🐝\n"
        "Чтобы синхронизироваться с вашей учеткой введите в своем профиле на сайте в "
        f"качестве Telegram ID этот: `{message.from_user.id}`",
        parse_mode="markdownv2"
    )
