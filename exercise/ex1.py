
number = int(input("Введите число: "))
if number % 2 == 0:
	print("Число чётное")
else:
	print("Число нечётное")


def deep_sum(obj):
    total = 0
    if isinstance(obj, dict):
        for val in obj.values():
            total += deep_sum(val)
    elif isinstance(obj, list):
        for val in obj:
            total += deep_sum(val)
    elif isinstance(obj, (int, float)):
        total += obj
    return total


lst = [
    {1: 11, 2: 12, 3: 13},
    {1: 21, 2: 22, 3: 23},
    {1: 24, 2: 25, 3: 26},
]

print(deep_sum(lst))  
