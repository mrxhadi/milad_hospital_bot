# استفاده از تصویر رسمی Python
FROM python:3.10-slim

# تعیین دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل‌های پروژه به کانتینر
COPY . /app

# نصب پکیج‌های مورد نیاز
RUN pip install --no-cache-dir -r requirements.txt

# نصب مرورگر کروم و کروم درایور
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    chromium-driver

# تنظیم متغیرهای محیطی برای استفاده از کروم در Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

# دستور اجرا
CMD ["python", "bot/main.py"]
