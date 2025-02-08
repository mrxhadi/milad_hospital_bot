# استفاده از تصویر پایه Python
FROM python:3.10-slim

# تنظیمات برای کپی کردن فایل‌ها
WORKDIR /app
COPY . .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# اجرای برنامه
CMD ["python", "main.py"]
