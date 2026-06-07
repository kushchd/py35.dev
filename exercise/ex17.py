def sum_of_divisors(n: int) -> int:
    """Возвращает сумму собственных делителей числа n"""
    divisors_sum = 1  # 1 всегда делитель
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:
                divisors_sum += n // i
    return divisors_sum

# Ввод чисел
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

# Проверка
if sum_of_divisors(a) == b and sum_of_divisors(b) == a:
    print(f"{a} и {b} являются дружественными числами")
else:
    print(f"{a} и {b} не являются дружественными числами")
