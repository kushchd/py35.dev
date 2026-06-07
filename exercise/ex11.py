from datetime import date

print(date.today().strftime("%Y-%m-%d"))


from datetime import datetime

print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


# Просим пользователя ввести два целых числа
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Определяем минимальное и максимальное
start = min(a, b)
end = max(a, b)

# Формируем список всех целых чисел от минимального до максимального включительно
numbers = list(range(start, end + 1))

# Выводим результат
print(numbers)
