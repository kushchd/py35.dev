numbers = [x for x in range(1, 23, 3)]
print(numbers)


# делим список на две половины
mid = len(numbers) // 2
first_half = numbers[:mid]   # [1, 2, 3]
second_half = numbers[mid:]  # [4, 5, 6]

# считаем суммы
sum_first = sum(first_half)   # 6
sum_second = sum(second_half) # 15

# делим
result = sum_first / sum_second
print(result)  # 0.4

st1 = {1, 2, 3, 4, 5, 6}
st2 = {4, 5, 6, 7, 8}

common = st1 & st2
print(common)  # {4, 5}


num = 50
zeros = "0" * num
print(zeros)  # 00000
