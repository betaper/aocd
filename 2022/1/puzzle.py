# Standard library
from locale import atoi
import sys

# Local modules
import aocd

lines = aocd.read(sys.argv[1])

calories = []
total = 0
for line in lines:
    if line == '':
        calories.append(total)
        total = 0
    else:
        total += atoi(line)
calories.append(total)  # add last elf's calories
calories.sort()
answer1 = calories[-1]
answer2 = sum(calories[-3:])

print(f'Answer 1: {answer1}')
print(f'Answer 2: {answer2}')
