from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# توکن ربات
TOKEN = '8049424440:AAGBPPfMynEI-8PRsZdA-XfcvUauOxwvAzY'

def start(update, context):
    update.message.reply("سلام! من ربات شما هستم. لطفاً کد ملی خود را وارد کنید.")

def handle_message(update, context):
    # اینجا بررسی می‌کنیم که آیا پیام یک عدد ۱۰ رقمی است
    if len(update.message.text) == 10 and update.message.text.isdigit():
        update.message.reply(f"کد ملی شما {update.message.text} ثبت شد!")
    else:
        update.message.reply("لطفاً یک کد ملی معتبر وارد کنید.")

def main():
    updater = Updater(token=TOKEN, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
