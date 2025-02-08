import sqlite3
import threading
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from apscheduler.schedulers.background import BackgroundScheduler
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# تنظیمات دیتابیس
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    national_code TEXT
)
""")
conn.commit()

def save_national_code(user_id, national_code):
    cursor.execute("REPLACE INTO users (user_id, national_code) VALUES (?, ?)", (user_id, national_code))
    conn.commit()

def get_national_code(user_id):
    cursor.execute("SELECT national_code FROM users WHERE user_id=?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else None

def delete_national_code(user_id):
    cursor.execute("DELETE FROM users WHERE user_id=?", (user_id,))
    conn.commit()

# تلگرام بات
def start(update: Update, context: CallbackContext):
    update.message.reply_text("سلام! لطفاً کد ملی خود را وارد کنید تا نوبت شما بررسی شود.")

def set_national_code(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    national_code = update.message.text

    if len(national_code) != 10 or not national_code.isdigit():
        update.message.reply_text("❌ کد ملی نامعتبر است! لطفاً یک کد ۱۰ رقمی وارد کنید.")
        return

    save_national_code(user_id, national_code)
    update.message.reply_text(f"✅ کد ملی شما ذخیره شد: {national_code}")

def get_status(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    national_code = get_national_code(user_id)

    if national_code:
        update.message.reply_text(f"✅ کد ملی شما: {national_code}\nربات در حال بررسی نوبت‌هاست...")
    else:
        update.message.reply_text("❌ شما هنوز کد ملی خود را ثبت نکرده‌اید!")

def delete_national_code_command(update: Update, context: CallbackContext):
    user_id = update.message.chat_id
    delete_national_code(user_id)
    update.message.reply_text("✅ کد ملی شما حذف شد. اگر می‌خواهید دوباره ثبت کنید، کد ملی جدید را ارسال کنید.")

# تنظیم دستورات تلگرام
def main():
    updater = Updater("TELEGRAM_BOT_TOKEN", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, set_national_code))
    dp.add_handler(CommandHandler("status", get_status))
    dp.add_handler(CommandHandler("delete", delete_national_code_command))

    updater.start_polling()
    updater.idle()

threading.Thread(target=main).start()

# اتوماسیون Selenium
def check_and_book_nobat(national_code):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    driver.get("https://miladhospital.com/onlineReception")
    time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(text(), 'قبول قوانین')]").click()
    time.sleep(2)

    input_box = driver.find_element(By.NAME, "nationalCode")
    input_box.send_keys(national_code)
    input_box.send_keys(Keys.RETURN)
    time.sleep(5)

    clinics = driver.find_elements(By.CSS_SELECTOR, ".clinic-item")
    if not clinics:
        print(f"❌ نوبتی برای کد ملی {national_code} پیدا نشد.")
        driver.quit()
        return False

    for clinic in clinics:
        if "رزرو نوبت" in clinic.text:
            clinic.click()
            time.sleep(3)
            break
    else:
        print(f"❌ هیچ درمانگاهی نوبت خالی ندارد برای {national_code}.")
        driver.quit()
        return False

    doctors = driver.find_elements(By.CSS_SELECTOR, ".doctor-item")
    if doctors:
        doctors[0].click()
        time.sleep(3)

    shifts = driver.find_elements(By.CSS_SELECTOR, ".shift-item")
    if shifts:
        shifts[0].click()
        time.sleep(3)

    driver.find_element(By.XPATH, "//button[contains(text(), 'تأیید')]").click()
    time.sleep(3)

    print(f"✅ نوبت با موفقیت برای {national_code} رزرو شد!")
    driver.quit()
    return True

scheduler = BackgroundScheduler()

def schedule_nobat_checks():
    cursor.execute("SELECT national_code FROM users")
    users = cursor.fetchall()

    for user in users:
        national_code = user[0]
        if check_and_book_nobat(national_code):
            print(f"✅ نوبت برای {national_code} گرفته شد.")

scheduler.add_job(schedule_nobat_checks, "interval", minutes=30)
scheduler.start()