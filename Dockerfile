# مرحله اول: استفاده از تصویر پایه Python
FROM python:3.10-slim

# نصب پکیج‌های مورد نیاز
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    chromium \
    && apt-get clean

# نصب پکیج‌های مورد نیاز برای Selenium
RUN pip install --upgrade pip
RUN pip install selenium python-telegram-bot aiogram

# تنظیم متغیرهای محیطی برای Selenium و Chrome
ENV DISPLAY=:99
ENV CHROMIUM_BIN=/usr/bin/chromium
ENV CHROMIUM_PATH=/usr/lib/chromium

# ایجاد پوشه برای اپلیکیشن
WORKDIR /app

# کپی کردن فایل‌های پروژه به داکر
COPY . /app

# نصب نیازمندی‌ها از requirements.txt
RUN pip install -r requirements.txt

# باز کردن پورت‌های مورد نیاز
EXPOSE 8000

# اجرای فایل main.py
CMD ["python", "bot/main.py"]
