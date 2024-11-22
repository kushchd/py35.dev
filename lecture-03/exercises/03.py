#
def max_n(lst, n):
        x = sorted(lst, reverse=True)
        return x[:n]

result_1 = max_n([1, 2, 3], 1)
print(result_1) 

result_2 = max_n([1, 2, 3], 2)
print(result_2) 
