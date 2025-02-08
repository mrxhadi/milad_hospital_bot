# استفاده از تصویر پایه پایتون
FROM python:3.12-slim

# نصب وابستگی‌ها
RUN apt-get update && apt-get install -y \
    chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# نصب پکیج‌های پایتون
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن کدهای پروژه
COPY . /app

# تنظیمات دایرکتوری کاری
WORKDIR /app

# اجرای ربات
CMD ["python", "bot.py"]
