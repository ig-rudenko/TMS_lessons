from aiogram import Router, types

router = Router()


@router.message()
async def other(message: types.Message):
    """Для всех других сообщений"""
    await message.answer("Я не понимаю")
