from datetime import datetime

def time_until_day_month(date_str: str) -> dict:
    """
    date_str — строка в формате 'DD-MM' или 'DD.MM'
    Возвращает словарь с количеством дней, часов, минут и секунд до указанной даты (00:00).
    """
    now = datetime.now()

    # Поддержка двух разделителей: '-' и '.'
    if "-" in date_str:
        day, month = map(int, date_str.split("-"))
    elif "." in date_str:
        day, month = map(int, date_str.split("."))
    else:
        raise ValueError("Введите дату в формате DD-MM или DD.MM")

    # Формируем дату в текущем году
    target = datetime(year=now.year, month=month, day=day)

    # Если дата уже прошла — берём следующий год
    if target <= now:
        target = datetime(year=now.year + 1, month=month, day=day)

    delta = target - now

    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {"d": days, "h": hours, "m": minutes, "s": seconds}


# Ввод от оператора
user_input = input("Введите дату в формате DD-MM или DD.MM: ")
result = time_until_day_month(user_input)
print("До указанной даты осталось:", result)
