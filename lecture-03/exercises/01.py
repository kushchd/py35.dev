#
def every_nth(list, n):
    return list[n-1::n]

result = every_nth([1, 2, 3, 4, 5, 6], 2)
print(result)
