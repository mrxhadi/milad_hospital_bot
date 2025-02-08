import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext
from telegram import Update

# فعال کردن logging برای نمایش خطاها و اطلاعات
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# دستور start که وقتی کاربر "/start" را ارسال می‌کند، اجرا می‌شود
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('سلام! من ربات نوبت‌گیری بیمارستان میلاد هستم.')

# دستور برای تغییر کد ملی
def change_id(update: Update, context: CallbackContext) -> None:
    # اینجا می‌توانید منطق تغییر کد ملی را پیاده‌سازی کنید
    update.message.reply_text('لطفاً کد ملی جدید خود را وارد کنید.')

# هندلر برای بررسی متن پیام‌ها و پاسخ به آن‌ها
def handle_message(update: Update, context: CallbackContext) -> None:
    text = update.message.text.lower()
    
    # بررسی اگر کاربر کلمه خاصی ارسال کرد
    if 'نوبت' in text:
        update.message.reply_text('در حال بررسی نوبت‌ها...')
        # اینجا منطق بررسی نوبت‌ها با استفاده از Selenium می‌آید.
    else:
        update.message.reply_text(f'شما نوشتید: {update.message.text}')

# هندلر خطاها
def error(update: Update, context: CallbackContext) -> None:
    logger.warning('حدس زده شده خطا: %s', context.error)

# تابع اصلی که ربات را اجرا می‌کند
def main():
    # توکن ربات تلگرام شما
    token = "YOUR_BOT_API_TOKEN"

    # ایجاد Updater و Dispatcher
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    
    # اضافه کردن هندلرها
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("change_id", change_id))
    dispatcher.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # هندلر برای خطاها
    dispatcher.add_error_handler(error)
    
    # شروع Polling و فعال‌سازی ربات
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
