# Standard library
import sys
from locale import atoi

# Local modules
import aocd

opponent = {'A': 1, 'B': 2, 'C': 3}  # 1=Rock, 2=paper, 3=scissors
me = {'X': 1, 'Y': 2, 'Z': 3}

lines = aocd.read(sys.argv[1])

total_score = 0
for line in lines:
    choices = line.split()
    my_choice = me[choices[1]]
    result = my_choice - opponent[choices[0]]
    if result == 1 or result == -2:
        score = 6  # win
    if result == 2 or result == -1:
        score = 0  # loss
    if result == 0:
        score = 3  # draw
    score += my_choice
    total_score += score

print(f'Answer: {total_score}')




