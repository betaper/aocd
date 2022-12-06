# Standard library
import sys
from locale import atoi

# Local modules
import aocd

if len(sys.argv) == 1:
    print(
        'Usage: puzzle.py input_file [n_char]\n',
        '\n',
        'Parameters\n',
        '----------\n',
        'input_file: example.txt or input.txt\n',
        'n_char: number of distinct characters (default=4)'
        )
    sys.exit()

line = aocd.read(sys.argv[1])[0]

try:
    n_char = atoi(sys.argv[2])
except IndexError:
    n_char = 4

i = 0
while True:
    if len(set(line[i: i + n_char])) == n_char:
        break
    i += 1

print(f'Answer: {i + n_char}')

