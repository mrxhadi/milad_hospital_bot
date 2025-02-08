import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from dotenv import load_dotenv
import os

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# تنظیمات لاگ‌گیری
logging.basicConfig(level=logging.INFO)

# توکن ربات از متغیر محیطی
TOKEN = os.getenv("8049424440:AAGBPPfMynEI-8PRsZdA-XfcvUauOxwvAzY")

# ایجاد نمونه‌های Bot و Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# ثبت Middleware برای لاگ‌گیری
dp.middleware.setup(LoggingMiddleware())

# دستورات ربات
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("سلام! من ربات هستم. چطور می‌توانم به شما کمک کنم؟")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.answer("برای استفاده از ربات، فقط دستورات /start و /help را وارد کنید.")

@dp.message_handler(content_types=types.ContentType.TEXT)
async def echo_message(message: types.Message):
    await message.answer(f"شما گفتید: {message.text}")

# راه‌اندازی ربات
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
