from datetime import datetime

# Запрашиваем дату и время рождения
birth_str = input("Введите дату и время рождения (год-месяц-день часы:минуты): ")
birth_date = datetime.strptime(birth_str, "%Y-%m-%d %H:%M")

# Текущая дата и время
now = datetime.now()

# --- Полные годы ---
years = now.year - birth_date.year
if (now.month, now.day, now.hour, now.minute) < (birth_date.month, birth_date.day, birth_date.hour, birth_date.minute):
    years -= 1

# --- Полные месяцы ---
months = now.month - birth_date.month
if months < 0:
    months += 12
if (now.day, now.hour, now.minute) < (birth_date.day, birth_date.hour, birth_date.minute):
    months -= 1
    if months < 0:
        months += 12

# --- Полные дни ---
days = now.day - birth_date.day
if days < 0:
    # берём количество дней в предыдущем месяце
    prev_month = (now.month - 1) if now.month > 1 else 12
    prev_year = now.year if now.month > 1 else now.year - 1
    days_in_prev_month = (datetime(prev_year, prev_month + 1, 1) - datetime(prev_year, prev_month, 1)).days
    days += days_in_prev_month

# --- Полные часы ---
hours = now.hour - birth_date.hour
if hours < 0:
    hours += 24
    days -= 1
    if days < 0:
        days = 0  # упрощённая коррекция

# --- Вывод ---
print(f"Вам {years} лет, {months} месяцев, {days} дней и {hours} часов.")
