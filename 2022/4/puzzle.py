# Standard library
import sys
from locale import atoi

# Local modules
import aocd

lines = aocd.read(sys.argv[1])

n_inc = 0
n_overlap = 0
for line in lines:
    section_sets = []
    for section in line.split(','):
        start, stop = section.split('-')
        section_set = set(range(atoi(start), atoi(stop) + 1))
        section_sets.append(section_set)
    set1, set2 = section_sets
    intersect = set1 & set2
    if len(intersect) > 0:
        n_overlap += 1
        if intersect == set1 or intersect == set2:
            n_inc += 1

print(f'Answer 1: {n_inc}')
print(f'Answer 2: {n_overlap}')

