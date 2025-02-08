import subprocess
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# تابع برای بررسی نسخه‌ی python-telegram-bot
def get_pip_version():
    result = subprocess.run(["pip", "show", "python-telegram-bot"], stdout=subprocess.PIPE)
    return result.stdout.decode()

# دستور start
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("سلام! من ربات بیمارستان میلاد هستم.")
    
    # بررسی نسخه‌ی کتابخانه python-telegram-bot و ارسال آن به کاربر
    pip_version = get_pip_version()
    await update.message.reply_text(f"نسخه python-telegram-bot: \n{pip_version}")

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
