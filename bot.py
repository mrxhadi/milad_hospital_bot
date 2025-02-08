import logging
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
import os

# بارگذاری توکن از متغیر محیطی
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# تنظیمات لاگ‌گیری
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# تعریف دیکشنری برای ذخیره کد ملی هر کاربر
user_national_code = {}

# منو اصلی با گزینه‌ها
def get_main_menu():
    return ReplyKeyboardMarkup([['رزرو نوبت', 'تغییر کد ملی'], ['کمک']], one_time_keyboard=True)

# Start command
async def start(update: Update, context: CallbackContext) -> None:
    # ارسال پیام خوشامدگویی با منو
    await update.message.reply_text('سلام! من ربات نوبت‌دهی بیمارستان میلاد هستم. لطفاً یک گزینه را انتخاب کنید:', reply_markup=get_main_menu())

# ثبت کد ملی کاربر
async def set_national_code(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    code = update.message.text.strip()
    
    # ذخیره کد ملی کاربر در دیکشنری
    user_national_code[user_id] = code
    await update.message.reply_text(f'کد ملی شما به {code} تنظیم شد.')

# دستور رزرو نوبت
async def book_appointment(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    if user_id not in user_national_code:
        await update.message.reply_text('لطفاً ابتدا کد ملی خود را وارد کنید.')
        return

    national_code = user_national_code[user_id]
    await update.message.reply_text(f'در حال جستجو برای نوبت با کد ملی {national_code}...')

    # فراخوانی تابع رزرو نوبت
    result = await start_appointment_process(national_code)

    await update.message.reply_text(result)

# دستور تغییر کد ملی
async def change_national_code(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('لطفاً کد ملی جدید خود را وارد کنید.')

# دستور کمک
async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = """
    1. **رزرو نوبت**: برای رزرو نوبت، کد ملی خود را وارد کنید.
    2. **تغییر کد ملی**: اگر می‌خواهید کد ملی خود را تغییر دهید، از این گزینه استفاده کنید.
    """
    await update.message.reply_text(help_text)

# تابع رزرو نوبت (شما باید این تابع را برای شروع فرآیند نوبت‌گیری از سایت میلاد اضافه کنید)
async def start_appointment_process(national_code: str) -> str:
    # این تابع باید تمامی مراحل رزرو نوبت را با استفاده از Selenium مدیریت کند
    # که به طور مداوم سایت را بررسی می‌کند
    # و نوبت را رزرو می‌کند.
    return "رزرو نوبت با موفقیت انجام شد."

# Main function to start the bot
def main():
    application = Application.builder().token(TOKEN).build()

    # Handlers for commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, set_national_code))
    application.add_handler(CommandHandler("book", book_appointment))
    application.add_handler(CommandHandler("help", help_command))
    
    # Handlers for menu options
    application.add_handler(MessageHandler(filters.Regex('رزرو نوبت'), book_appointment))
    application.add_handler(MessageHandler(filters.Regex('تغییر کد ملی'), change_national_code))
    application.add_handler(MessageHandler(filters.Regex('کمک'), help_command))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
