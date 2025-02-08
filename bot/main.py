import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor

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
    await message.reply("سلام! من ربات شما هستم.")

if __name__ == "__main__":
    # اجرای ربات
    executor.start_polling(dp, skip_updates=True)
