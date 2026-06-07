number = int(input("Введите число: "))
first_digit = str(number)[0]
last_digital = str(number)[-1]
print("Первая цифра числа:", first_digit)
print("Последняя цифра:", last_digital)

print("Количество цифр:", len(str(abs(number))))

digit_sum = sum(int(digit) for digit in str(abs(number)))
print("Сумма цифр:", digit_sum)

reversed_number = int(str(number)[::-1])
print("Перевернутое число:", reversed_number)


digits_dict = {i: int(d) for i, d in enumerate(str(abs(number)))}     # умножаем цифры на 2
print("Исходный словарь:", digits_dict)
doubled_dict = {key: value * 2 for key, value in digits_dict.items()}
print("Удвоенный словарь:", doubled_dict)
