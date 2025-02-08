# انتخاب تصویر پایه
FROM python:3.10-slim

# نصب وابستگی‌ها
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    && apt-get clean

# ایجاد و تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های پروژه
COPY . .

# نصب پکیج‌ها از requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# اجرای برنامه
CMD ["python", "main.py"]
