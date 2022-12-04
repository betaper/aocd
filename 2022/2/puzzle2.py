# Standard library
import sys
from locale import atoi

# Local modules
import aocd

opponent = {'A': 1, 'B': 2, 'C': 3}  # Rock, paper, scissors
results = {'X': -1, 'Y': 0, 'Z': 1}  # Loose, draw, win

lines = aocd.read(sys.argv[1])

total_score = 0
for line in lines:
    choices = line.split()
    opponent_choice = opponent[choices[0]]
    result = results[choices[1]]
    my_choice = opponent_choice + result
    if my_choice == 0:
        my_choice = 3
    if my_choice == 4:
        my_choice = 1
    score = (result + 1) * 3 + my_choice
    total_score += score

print(f'Answer: {total_score}')




