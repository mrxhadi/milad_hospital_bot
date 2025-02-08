from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# تنظیمات مرورگر
chrome_options = Options()
chrome_options.add_argument("--headless")  # برای اجرای در حالت بدون نمایش
chrome_options.add_argument("--disable-gpu")

# راه‌اندازی WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# باز کردن سایت بیمارستان میلاد
driver.get("https://miladhospital.com/onlineReception")

# صبر برای بارگذاری کامل صفحه
time.sleep(5)

# استخراج تعداد پزشکان
doctors = []
doctor_elements = driver.find_elements(By.XPATH, '//*[@class="doctor-class"]')  # XPath باید به‌درستی تنظیم شود
for doctor in doctor_elements:
    doctors.append(doctor.text)

# حالا که لیست پزشکان را داریم، می‌توانیم به ترتیب روی هر دکتر کلیک کنیم
for i, doctor in enumerate(doctors, start=1):
    # ساخت XPath داینامیک با شماره دکتر
    doctor_xpath = f'//*[@id="select_container_{i}"]'  # فرض: پزشکان با شماره 1، 2، 3 ... مشخص می‌شوند
    try:
        # کلیک بر روی دکتر
        doctor_element = driver.find_element(By.XPATH, doctor_xpath)
        doctor_element.click()  # کلیک کردن روی دکتر
        time.sleep(2)  # منتظر می‌مانیم تا اطلاعات بارگذاری شود

        # می‌توانید اینجا اطلاعات مربوط به شیفت‌ها و پزشک را استخراج کنید
        # مثلاً اگر شیفت‌ها بعد از کلیک روی دکتر بارگذاری می‌شوند
        shift_elements = driver.find_elements(By.XPATH, '//*[@class="shift-class"]')  # XPath شیفت‌ها
        shifts = [shift.text for shift in shift_elements]

        print(f"پزشک {doctor}: شیفت‌ها: {shifts}")
    except Exception as e:
        print(f"خطا در پیدا کردن دکتر {doctor} با شماره {i}: {e}")

# بستن مرورگر
driver.quit()

# چاپ اطلاعات استخراج‌شده
print("Doctors:", doctors)
