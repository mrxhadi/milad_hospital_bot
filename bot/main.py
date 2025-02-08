import telepot
from telepot.loop import MessageLoop
import time

# توکن ربات تلگرام
bot = telepot.Bot('8049424440:AAGBPPfMynEI-8PRsZdA-XfcvUauOxwvAzY')

# تابع برای پاسخ به پیام‌ها
def handle_message(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    if command == '/start':
        bot.sendMessage(chat_id, "سلام! من ربات شما هستم.")
    else:
        bot.sendMessage(chat_id, "متاسفم، من این دستور را نمی‌شناسم.")

# شروع دریافت پیام‌ها
MessageLoop(bot, handle_message).run_as_thread()

# نگه داشتن ربات در حال اجرا
while True:
    time.sleep(10)
