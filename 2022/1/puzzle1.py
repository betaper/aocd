from locale import atoi
import sys

with open(sys.argv[1], 'r') as file:
    lines = file.readlines()

calories = []
total = 0
for line in lines:
    if line == '\n':
        calories.append(total)
        total = 0
    else:
        total += atoi(line)
calories.append(total)  # add last elf's result
calories.sort()
answer1 = calories[-1]
answer2 = sum(calories[-3:])

print(f'Answer 1: {answer1}')
print(f'Answer 2: {answer2}')
