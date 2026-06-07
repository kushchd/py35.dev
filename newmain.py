def process_numbers(input_string):
    # Разделяем входную строку по запятым и преобразуем в список целых чисел
    numbers = list(map(int, input_string.split(',')))

    # Формируем два списка: один для четных, другой для нечетных чисел
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Выводим списки без скобок и на отдельных строках
    print(' '.join(map(str, odd_numbers)))
    print(' '.join(map(str, even_numbers)))

# Пример использования
input_string = "3,4,2,7,8,9,1,11,2,56,2,6,81"
process_numbers(input_string)


# Вводим число
number = float(input("Введите число: "))

# Проверяем, отрицательное ли это число
if number < 0:
    print("Число отрицательное.")
else:
    print("Число не является отрицательным.")

# Вводим строку
text = input("Введите строку: ")

# Выводим длину строки
print("Длина строки:", len(text))

# Вводим два слова
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

# Проверяем, совпадают ли первые буквы
if word1[0].lower() == word2[0].lower():
    print("Первые буквы совпадают.")
else:
    print("Первые буквы не совпадают.")
