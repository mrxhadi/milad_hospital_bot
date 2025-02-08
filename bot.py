import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from dotenv import load_dotenv
import os

# بارگذاری متغیرهای محیطی از فایل .env (اگر استفاده کنید) یا از Railway
load_dotenv()

# توکن ربات از متغیر محیطی
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# تنظیمات لاگ‌گیری
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# متغیر سراسری برای کد ملی
user_national_code = {}

# Start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! برای رزرو نوبت، لطفاً کد ملی خود را وارد کنید.')

# ثبت کد ملی کاربر
def set_national_code(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    code = update.message.text.strip()
    
    # ذخیره کد ملی کاربر
    user_national_code[user_id] = code
    update.message.reply_text(f'کد ملی شما به {code} تنظیم شد.')

# دستور رزرو نوبت
def book_appointment(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_national_code:
        update.message.reply_text('لطفاً ابتدا کد ملی خود را وارد کنید.')
        return

    national_code = user_national_code[user_id]
    update.message.reply_text(f'در حال جستجو برای نوبت با کد ملی {national_code}...')

    # فراخوانی تابع رزرو نوبت
    # (شما باید این تابع رو برای شروع فرآیند نوبت‌گیری از سایت میلاد اضافه کنید)
    result = start_appointment_process(national_code)

    update.message.reply_text(result)

def start_appointment_process(national_code: str) -> str:
    # این تابع باید تمامی مراحل رزرو نوبت را با استفاده از Selenium مدیریت کند
    # که به طور مداوم سایت را بررسی می‌کند
    # و نوبت را رزرو می‌کند.
    return "رزرو نوبت با موفقیت انجام شد."

# Main function to start the bot
def main():
    # Replace 'YOUR_TOKEN' with your bot's token
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher

    # Handlers for commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    dispatcher.add_handler(CommandHandler("book", book_appointment))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
