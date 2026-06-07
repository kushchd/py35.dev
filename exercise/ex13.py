def divisors(n: int):
    n = abs(n)  # работаем с модулем числа
    if n == 0:
        return None  # у нуля бесконечно много делителей
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

# ввод числа оператором
number = int(input("Введите целое число: "))

divs = divisors(number)
if divs is None:
    print("У числа 0 бесконечно много делителей.")
else:
    print("Количество делителей:", len(divs))
    print("Сами делители:", divs)
