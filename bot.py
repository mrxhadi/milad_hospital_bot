import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
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

# لیست درمانگاه‌ها، پزشکان و شیفت‌ها
clinics = ['درمانگاه 1', 'درمانگاه 2', 'درمانگاه 3']
doctors = {
    'درمانگاه 1': ['پزشک 1', 'پزشک 2'],
    'درمانگاه 2': ['پزشک 3', 'پزشک 4'],
    'درمانگاه 3': ['پزشک 5', 'پزشک 6']
}
shifts = {
    'پزشک 1': ['شیفت 1', 'شیفت 2'],
    'پزشک 2': ['شیفت 1', 'شیفت 3'],
    'پزشک 3': ['شیفت 2', 'شیفت 4'],
    'پزشک 4': ['شیفت 3', 'شیفت 5'],
    'پزشک 5': ['شیفت 1', 'شیفت 4'],
    'پزشک 6': ['شیفت 2', 'شیفت 5']
}

# منو اصلی با گزینه‌ها
def get_main_menu():
    return InlineKeyboardMarkup([[
        InlineKeyboardButton("رزرو نوبت", callback_data='book'),
        InlineKeyboardButton("تغییر کد ملی", callback_data='set_national_code')
    ], [
        InlineKeyboardButton("کمک", callback_data='help')
    ]])

# منوی درمانگاه‌ها
def get_clinics_menu():
    keyboard = [[InlineKeyboardButton(clinic, callback_data=f'clinic_{clinic}')] for clinic in clinics]
    return InlineKeyboardMarkup(keyboard)

# منوی پزشکان بر اساس درمانگاه انتخاب‌شده
def get_doctors_menu(clinic):
    doctors_list = doctors.get(clinic, [])
    keyboard = [[InlineKeyboardButton(doctor, callback_data=f'doctor_{doctor}')] for doctor in doctors_list]
    return InlineKeyboardMarkup(keyboard)

# منوی شیفت‌ها بر اساس پزشک انتخاب‌شده
def get_shifts_menu(doctor):
    shifts_list = shifts.get(doctor, [])
    keyboard = [[InlineKeyboardButton(shift, callback_data=f'shift_{shift}')] for shift in shifts_list]
    return InlineKeyboardMarkup(keyboard)

# Start command
async def start(update: Update, context: CallbackContext) -> None:
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

    # ارسال منوی درمانگاه‌ها
    await update.message.reply_text("لطفاً درمانگاه خود را انتخاب کنید:", reply_markup=get_clinics_menu())

# دستور کمک
async def help_command(update: Update, context: CallbackContext) -> None:
    help_text = """
    1. **رزرو نوبت**: برای رزرو نوبت، کد ملی خود را وارد کنید.
    2. **تغییر کد ملی**: اگر می‌خواهید کد ملی خود را تغییر دهید، از این گزینه استفاده کنید.
    """
    await update.message.reply_text(help_text)

# واکنش به انتخاب درمانگاه
async def clinic_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    clinic = query.data.split('_')[1]  # دریافت نام درمانگاه انتخاب‌شده
    # ارسال منوی پزشکان مربوط به درمانگاه
    await query.edit_message_text(f"لطفاً پزشک مورد نظر خود را از {clinic} انتخاب کنید:", reply_markup=get_doctors_menu(clinic))

# واکنش به انتخاب پزشک
async def doctor_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    doctor = query.data.split('_')[1]  # دریافت نام پزشک انتخاب‌شده
    # ارسال منوی شیفت‌ها مربوط به پزشک
    await query.edit_message_text(f"لطفاً شیفت مورد نظر برای {doctor} را انتخاب کنید:", reply_markup=get_shifts_menu(doctor))

# واکنش به انتخاب شیفت
async def shift_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    await query.answer()
    shift = query.data.split('_')[1]  # دریافت نام شیفت انتخاب‌شده
    # تایید رزرو نوبت
    await query.edit_message_text(f"نوبت شما با شیفت {shift} رزرو شد.")

# Main function to start the bot
def main():
    application = Application.builder().token(TOKEN).build()

    # Handlers for commands
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, set_national_code))
    application.add_handler(CommandHandler("book", book_appointment))
    application.add_handler(CommandHandler("help", help_command))

    # Handlers for callback queries (Inline Keyboard)
    application.add_handler(MessageHandler(filters.Regex('book'), book_appointment))
    application.add_handler(MessageHandler(filters.Regex('set_national_code'), set_national_code))
    application.add_handler(MessageHandler(filters.Regex('help'), help_command))

    application.add_handler(CallbackQueryHandler(clinic_callback, pattern='^clinic_'))
    application.add_handler(CallbackQueryHandler(doctor_callback, pattern='^doctor_'))
    application.add_handler(CallbackQueryHandler(shift_callback, pattern='^shift_'))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()
