from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# تنظیمات مرورگر
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

def book_appointment_with_selenium(national_code: str):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get("https://miladhospital.com/onlineReception")

    # قبول قوانین و پذیرش
    time.sleep(2)
    driver.find_element(By.XPATH, '//button[contains(text(), "قبول قوانین")]').click()

    # وارد کردن کد ملی
    time.sleep(2)
    input_field = driver.find_element(By.ID, "national_code")
    input_field.send_keys(national_code)
    driver.find_element(By.XPATH, '//button[contains(text(), "ثبت کد ملی")]').click()

    # ادامه مراحل انتخاب درمانگاه، پزشک و شیفت
    time.sleep(3)
    # این قسمت را با توجه به ساختار دقیق سایت خود پیاده‌سازی کنید

    # اگر درمانگاه نوبت داشت، انتخاب کنید
    # اگر نوبت نداشت، هر نیم ساعت چک کنید

    driver.quit()
