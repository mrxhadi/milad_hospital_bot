import telepot
from telepot.loop import MessageLoop

# توکن ربات
TOKEN = 'توکن_شما_را_اینجا_قرار_دهید'

# تابعی که برای دریافت پیام‌ها و پاسخ به آن‌ها استفاده می‌شود
def handle(msg):
    chat_id = msg['chat']['id']
    text = msg['text']

    if text.lower() == '/start':
        bot.sendMessage(chat_id, "سلام! من ربات هستم.")
    elif text.lower() == '/help':
        bot.sendMessage(chat_id, "راهنما: می‌توانید دستور /start یا /help را وارد کنید.")
    else:
        bot.sendMessage(chat_id, "پیام شما دریافت شد!")

# ایجاد یک نمونه از ربات
bot = telepot.Bot(TOKEN)

# راه‌اندازی MessageLoop برای گوش دادن به پیام‌ها
MessageLoop(bot, handle).run_as_thread()

# ادامه کار برنامه (برای جلوگیری از بستن بلافاصله)
import time
while 1:
    time.sleep(10)
