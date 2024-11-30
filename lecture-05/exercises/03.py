#
from pathlib import Path

file_path = Path('text_peter.txt')

text = file_path.read_text()

num_lines = text.count('\n') + 1
num_words = len(text.split())
num_chars = len(text)

print(f'Кількість рядків: {num_lines}')
print(f'Кількість слів: {num_words}')
print(f'Кількість символів: {num_chars}')
