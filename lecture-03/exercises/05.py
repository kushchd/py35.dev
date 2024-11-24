#
def roll(lst, n):
    
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

print(roll([1, 2, 3, 4, 5], 2))
print(roll([1, 2, 3, 4, 5], -2))
