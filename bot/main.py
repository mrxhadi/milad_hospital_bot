import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# راه اندازی لاگینگ
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور شروع
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! من ربات شما هستم.")

# تابع main
async def main():
    # توکن ربات تلگرام خود را اینجا قرار دهید
    token = 'YOUR_BOT_TOKEN'

    # ایجاد نمونه‌ای از Application
    application = Application.builder().token(token).build()

    # اضافه کردن دستور /start
    application.add_handler(CommandHandler("start", start))

    # شروع polling برای دریافت پیام‌ها
    await application.run_polling()

if __name__ == "__main__":
    try:
        # اجرای ربات
        import asyncio
        asyncio.run(main())
    except Exception as e:
        logger.error(f"Error in bot: {e}")
