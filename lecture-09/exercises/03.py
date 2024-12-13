#
def sort_by_indexes(a, b, reverse=False):
    
    zipped_lists = zip(b, a)
    
    sorted_pairs = sorted(zipped_lists, key=lambda x: x[0], reverse=reverse)
    
    sorted_a = [x[1] for x in sorted_pairs]
    return sorted_a

a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]

print(sort_by_indexes(a, b))

print(sort_by_indexes(a, b, True))