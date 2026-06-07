def zodiac_sign(day: int, month: int) -> str:
    # Проверка корректности дня и месяца
    days_in_month = {
        1: 31, 2: 29, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    if month not in days_in_month or day < 1 or day > days_in_month[month]:
        return "Ошибка: некорректная дата"
    
    zodiac_dates = [
        ("Овен", (3,21), (4,19)),
        ("Телец", (4,20), (5,20)),
        ("Близнецы", (5,21), (6,20)),
        ("Рак", (6,21), (7,22)),
        ("Лев", (7,23), (8,22)),
        ("Дева", (8,23), (9,22)),
        ("Весы", (9,23), (10,22)),
        ("Скорпион", (10,23), (11,21)),
        ("Стрелец", (11,22), (12,21)),
        ("Козерог", (12,22), (1,19)),
        ("Водолей", (1,20), (2,18)),
        ("Рыбы", (2,19), (3,20)),
    ]
    
    for sign, (m1,d1), (m2,d2) in zodiac_dates:
        if (month == m1 and day >= d1) or (month == m2 and day <= d2):
            return sign
    return "Неизвестно"


if __name__ == "__main__":
    user_input = input("Введите дату в формате ДД.ММ: ")
    day, month = map(int, user_input.split("."))
    print("Ваш знак зодиака:", zodiac_sign(day, month))
