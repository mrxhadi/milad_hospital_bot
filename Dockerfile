# استفاده از تصویر رسمی Python
FROM python:3.10-slim

# نصب پیش‌نیازهای سیستم
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    chromium \
    chromium-driver \
    libgdk-pixbuf2.0-0 \
    libx11-xcb1 \
    libgbm1 \
    libxcomposite1 \
    libxrandr2 \
    libasound2 \
    libnss3 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libnspr4 \
    libxss1 \
    && rm -rf /var/lib/apt/lists/*

# تعیین دایرکتوری کاری داخل کانتینر
WORKDIR /app

# کپی کردن فایل‌های پروژه به کانتینر
COPY . /app

# نصب پکیج‌های مورد نیاز
RUN pip install --no-cache-dir -r requirements.txt

# تنظیم متغیرهای محیطی برای استفاده از کروم در Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROME_DRIVER=/usr/bin/chromedriver

# دستور اجرا
CMD ["python", "bot/main.py"]
