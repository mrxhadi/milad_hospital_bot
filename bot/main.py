from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# دستور start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("سلام! من ربات بیمارستان میلاد هستم.")

# تابع اصلی برای راه‌اندازی ربات
def main():
    # توکن ربات تلگرام خود را وارد کنید
    token = "YOUR_BOT_API_TOKEN"

    # راه‌اندازی Updater
    updater = Updater(token, use_context=True)

    # ثبت هندلرها
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # راه‌اندازی polling برای دریافت پیام‌ها
    updater.start_polling()

    # به‌طور مداوم کار ربات را اجرا نگه می‌دارد
    updater.idle()

if __name__ == "__main__":
    main()
