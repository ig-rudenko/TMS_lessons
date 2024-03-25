from aiogram import Router, types
from aiogram import F
from bs4 import BeautifulSoup
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.models import Recipe

router = Router()


@router.message(Command("recipes"))
async def show_recipes(message: types.Message):
    print("Пользователь", message.from_user.id, "отправил сообщение", message.text)
    recipes = await Recipe.first_10()
    text = ""
    builder = InlineKeyboardBuilder()

    for recipe in recipes:
        text += f"{recipe.name}\n"
        builder.add(types.InlineKeyboardButton(
            text=recipe.name,
            callback_data=f"recipe:{recipe.id}"
        ))

    builder.adjust(3)

    await message.answer(text, reply_markup=builder.as_markup())


@router.callback_query(F.data.startswith("recipe:"))
async def show_recipe(callback: types.CallbackQuery):
    recipe_id = callback.data.split(":")[-1]
    if not recipe_id.isdigit():
        await callback.message.answer("Неверный ID рецепта!")
        await callback.answer()
        return

    recipe = await Recipe.get(int(recipe_id))

    # Чтобы продемонстрировать BufferedInputFile, воспользуемся "классическим"
    # открытием файла через `open()`. Но, вообще говоря, этот способ
    # лучше всего подходит для отправки байтов из оперативной памяти
    # после проведения каких-либо манипуляций, например, редактированием через Pillow

    clear_text = get_text(recipe)
    text_parts: list[str] = []
    part = ""
    for letter in clear_text:
        if len(part) >= 1024:
            text_parts.append(part)
            part = ""
        part += letter

    with open(f"media/{recipe.preview_image}", "rb") as image_from_buffer:
        await callback.message.answer_photo(
            photo=types.BufferedInputFile(
                image_from_buffer.read(),
                filename=recipe.preview_image.split("/")[-1]
            ),
            caption=text_parts.pop(0),
            parse_mode="HTML",
        )

    for text in text_parts:
        await callback.message.answer(text)

    await callback.answer()  # Обязательно отвечаем (хотя бы пустым)


def get_text(recipe: Recipe) -> str:
    bs = BeautifulSoup(recipe.description, "html.parser")
    return bs.get_text()
