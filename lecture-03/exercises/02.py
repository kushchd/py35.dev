#
def min_n(lst, n):
        x = sorted(lst)
        return x[:n]

result_1 = min_n([1, 2, 3], 1)
print(result_1) 

result_2 = min_n([1, 2, 3], 2)
print(result_2) 
