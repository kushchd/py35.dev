#
def sort_dict_by_key(d, reverse=False):
    
    items = d.items()
    
    sorted_items = sorted(items, reverse=reverse)
    
    sorted_dict = dict(sorted_items)
    return sorted_dict


d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}


print(sort_dict_by_key(d))

print(sort_dict_by_key(d, True))