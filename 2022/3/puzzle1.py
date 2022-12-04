# Standard library
import sys

# Local modules
import aocd

lowercase_offset = 96
uppercase_offset = 38

lines = aocd.read(sys.argv[1])

total_priority = 0
for line in lines:
    no_items = len(line)
    comp1 = set(line[0: no_items // 2])
    comp2 = set(line[no_items // 2:])
    double_item = (comp1 & comp2).pop()
    priority = ord(double_item)
    if priority > lowercase_offset:
        priority -= lowercase_offset
    else:
        priority -= uppercase_offset
    total_priority += priority

print(f'Answer: {total_priority}')
