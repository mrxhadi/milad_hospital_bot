import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
import asyncio

API_TOKEN = '8049424440:AAGBPPfMynEI-8PRsZdA-XfcvUauOxwvAzY'  # توکن ربات شما

# تنظیمات لاگ
logging.basicConfig(level=logging.INFO)

# ایجاد شیء ربات و دیسپچر
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# دستورات ربات
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("سلام! من ربات شما هستم. از من چه کمکی می‌خواهید؟")

# ارسال پیام با استفاده از Markdown
@dp.message_handler(commands=['markdown'])
async def send_markdown(message: types.Message):
    await message.answer("این یک پیام *فرمت شده* است.", parse_mode=ParseMode.MARKDOWN)

# ارسال پیام با استفاده از HTML
@dp.message_handler(commands=['html'])
async def send_html(message: types.Message):
    await message.answer("این یک پیام <b>فرمت شده</b> است.", parse_mode=ParseMode.HTML)

# تابع اصلی که ربات را اجرا می‌کند
async def on_startup(dp):
    logging.info("Starting bot...")

# اجرای ربات
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, on_startup=on_startup)
