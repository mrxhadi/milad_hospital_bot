# استفاده از تصویر پایه Python
FROM python:3.10-slim

# نصب ابزارهای لازم
RUN apt-get update && apt-get install -y \
    gcc \
    libffi-dev \
    && apt-get clean

# تنظیمات برای کپی کردن فایل‌ها
WORKDIR /app
COPY . .

# نصب پکیج‌ها بدون محیط مجازی
RUN pip install --no-cache-dir -r requirements.txt

# اجرای برنامه
CMD ["python", "main.py"]
