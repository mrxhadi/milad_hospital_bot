import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import asyncio

# راه اندازی لاگینگ
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# توکن ربات تلگرام
TOKEN = '8049424440:AAGBPPfMynEI-8PRsZdA-XfcvUauOxwvAzY'

# ایجاد نمونه‌ای از Bot و Dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# دستور start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("سلام! من ربات شما هستم. لطفاً کد ملی خود را وارد کنید.")

# دستور وارد کردن کد ملی
@dp.message_handler()
async def handle_message(message: types.Message):
    # اینجا بررسی می‌کنیم که اگر پیام یک عدد 10 رقمی بود (کد ملی)
    if len(message.text) == 10 and message.text.isdigit():
        # ذخیره کد ملی در دیتابیس یا هر چیزی که می‌خواهید
        await message.reply(f"کد ملی شما {message.text} ثبت شد!")
    else:
        await message.reply("لطفاً یک کد ملی معتبر وارد کنید.")

# تابع اصلی که ربات را اجرا می‌کند
async def on_start():
    try:
        # در اینجا می‌توانید برای راه‌اندازی متدها و عملیات‌های دیگر در نظر بگیرید
        logger.info("ربات در حال اجراست...")
        await dp.start_polling()
    except Exception as e:
        logger.error(f"خطا در راه‌اندازی ربات: {e}")
        await bot.close()

if __name__ == "__main__":
    # اجرا با استفاده از asyncio
    asyncio.run(on_start())
