#
with open('text_peter.txt', 'r') as file:
    
    lines = file.read().splitlines()

lines.insert(2, 'If Peter Piper picked a peck of pickled peppers.')

with open('new_text_peter.txt', 'w') as file:
    for line in lines:
        file.write(line + '\n')
