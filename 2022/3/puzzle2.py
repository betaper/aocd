# Standard library
import sys

# Local modules
import aocd

lowercase_offset = 96
uppercase_offset = 38

lines = aocd.read(sys.argv[1])

total_priority = 0
for group in range(0, len(lines), 3):
    ruck1 = set(lines[group])
    ruck2 = set(lines[group + 1])
    ruck3 = set(lines[group + 2])
    badge = (ruck1 & ruck2 & ruck3).pop()
    priority = ord(badge)
    if priority > lowercase_offset:
        priority -= lowercase_offset
    else:
        priority -= uppercase_offset
    total_priority += priority

print(f'Answer: {total_priority}')
