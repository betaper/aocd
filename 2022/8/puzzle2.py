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
view_scores = []
for i in range(1, width-1):
    for j in range(1, depth-1):
        h = wood[i, j]
        sections = [
            np.flip(wood[i, 0:j]),
            wood[i, j+1:],
            np.flip(wood[0:i, j]),
            wood[i+1:, j]]
        view_score = 1
        for section in sections:
            view_dist = [i[0] for i in enumerate(section) if i[1] >= h]
            if view_dist == []:
                view_dist = len(section)  # no tree in the way up to the border
            else:
                view_dist = view_dist[0] + 1
            view_score *= view_dist
        view_scores.append(view_score)
print(f'Answer: {max(view_scores)}')
