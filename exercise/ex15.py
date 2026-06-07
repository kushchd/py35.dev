def convert_seconds(total_seconds: int) -> dict:
    days = total_seconds // 86400
    remainder = total_seconds % 86400

    hours = remainder // 3600
    remainder %= 3600

    minutes = remainder // 60
    seconds = remainder % 60

    return {'Дней': days, 'Часов': hours, 'Минут': minutes, 'Секунд': seconds}


def convert_seconds_divmod(total_seconds: int) -> dict:
    days, remainder = divmod(total_seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    return {'Дней': days, 'Часов': hours, 'Минут': minutes, 'Секунд': seconds}


# Ввод от оператора
user_input = int(input("Введите количество секунд: "))

# Первый вариант
result1 = convert_seconds(user_input)
print("Вариант 1:", result1)

# Второй вариант (через divmod)
result2 = convert_seconds_divmod(user_input)
print("Вариант 2:", result2)
