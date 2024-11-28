#
with open('sales.txt', 'r') as file:
     lines = file.readlines()
    
     for i, line in enumerate(lines):
        if 'laptop' in line:
            print(f'Рядок {i+1}: {line.strip()}')
