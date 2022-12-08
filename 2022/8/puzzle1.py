# Standard library
import sys
from locale import atoi
import numpy as np

# Local modules
import aocd

lines = aocd.read(sys.argv[1])

wood = []
for line in lines:
    wood.append([atoi(i) for i in line])
wood = np.array(wood)

width, depth = wood.shape
visible = 2 * (width + depth) - 4
for i in range(1, width-1):
    for j in range(1, depth-1):
        h = wood[i, j]
        sections = [
            wood[i, 0:j+1],
            wood[i, j:],
            wood[0:i+1, j],
            wood[i:, j]]
        for section in sections:
            max_section = np.max(section)
            if (list(section == max_section).count(True) == 1) and (h == max_section):
                visible += 1
                break

print(f'Answer: {visible}')
