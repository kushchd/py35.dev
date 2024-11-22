#
def includes_any(lst, values):
    for value in values:
        if value in lst:
            return True
    else:   
        return False

print(includes_any([1, 2, 3, 4], [2, 9]))  
print(includes_any([1, 2, 3, 4], [8, 9])) 
