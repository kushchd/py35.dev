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
