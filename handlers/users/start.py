
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.choose_auth import menu_editors

from loader import dp, bot


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")
    await bot.send_message(message.from_user.id, text="Select the desired button!", reply_markup=menu_editors)


