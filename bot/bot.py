from asyncio import run

from handlers import dp
from load import bot


async def start_bot():
    await dp.start_polling(bot)


if __name__ == "__main__":
    run(start_bot())