#
def average_by(lst, fn=lambda x: x):
    if not lst:
        raise ValueError("The list cannot be empty")
    
    mapped_values = list(map(fn, lst))
    
    total_sum = sum(mapped_values)
    
    avg_value = total_sum / len(mapped_values)
    
    return avg_value

data = [{'n': 4}, {'n': 2}, {'n': 8}, {'n': 6}]
result = average_by(data, lambda x: x['n'])
print(result)
