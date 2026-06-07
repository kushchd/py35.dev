def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            return "Ошибка: деление на ноль"
    else:
        return "Ошибка: неизвестный оператор"

# Запрашиваем у пользователя ввод
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operator = input("Введите математический оператор (+, -, *, /): ")

# Вычисляем результат
result = calculate(a, b, operator)
print(f"Результат: {result}")
