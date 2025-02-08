import logging
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# تنظیمات لاگینگ
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور start
async def start(update, context):
    await update.message.reply_text('سلام! من ربات بیمارستان میلاد هستم.')

# تابع اصلی برای راه‌اندازی ربات
async def main():
    # توکن ربات تلگرام خود را وارد کنید
    token = "YOUR_BOT_API_TOKEN"

    # راه‌اندازی Application
    application = Application.builder().token(token).build()

    # ثبت هندلرها
    application.add_handler(CommandHandler("start", start))

    try:
        # اجرای polling برای دریافت پیام‌ها
        await application.run_polling()
    except Exception as e:
        logger.error(f"Error in bot: {e}")
    finally:
        # پس از اتمام، ربات باید بسته شود
        await application.shutdown()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())  # از asyncio.run برای اجرای main استفاده می‌کنیم
