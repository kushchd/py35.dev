items = input("Введите элементы списка через пробел: ").split()

letters = sorted([x for x in items if x.isalpha()])
digits = sorted([int(x) for x in items if x.isdigit()])

print("Буквы:", letters)
print("Цифры:", digits)


text = "snake_case"

parts = text.split("_")  # ['snake', 'case']
camel = parts[0] + "".join(word.capitalize() for word in parts[1:])
print(camel)  # snakeCase


num = 123259
digits = str(abs(num))  # '123459'

is_increasing = True
for i in range(len(digits) - 1):
    if digits[i] >= digits[i + 1]:
        is_increasing = False
        break

print(is_increasing)  # True



# Все числа от 10 до 1000, у которых первая цифра четная
numbers = [num for num in range(10, 1001) if int(str(num)[0]) % 2 == 0]

print(numbers)

