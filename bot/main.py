from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# دستور start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("سلام! من ربات بیمارستان میلاد هستم.")

# تابع اصلی برای راه‌اندازی ربات
async def main():
    # توکن ربات تلگرام خود را وارد کنید
    token = "YOUR_BOT_API_TOKEN"

    # راه‌اندازی Application
    application = Application.builder().token(token).build()

    # ثبت هندلرها
    application.add_handler(CommandHandler("start", start))

    # راه‌اندازی polling برای دریافت پیام‌ها
    await application.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
