from aiogram import Dispatcher, Bot
from config.settings import Settings

settings = Settings()
bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()