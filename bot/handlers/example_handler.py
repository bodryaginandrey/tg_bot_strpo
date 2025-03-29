from aiogram import types
from aiogram.filters import CommandStart


from load import dp


@dp.message(CommandStart())
async def cmd_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.username}!")


@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)
