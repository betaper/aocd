# Standard library
import sys
from locale import atoi

# Local modules
import aocd

if len(sys.argv) == 1:
    print(
        'Usage: puzzle.py input_file [answer]\n',
        '  input_file: example.txt or input.txt\n',
        '  answer: 1 (default) or 2'
        )
    sys.exit()

lines = aocd.read(sys.argv[1])

# Which answer (default=1)?
try:
    ans = atoi(sys.argv[2])
except IndexError:
    ans = 1

# Parse initial stacking
stacks = {}
while True:
    line = lines.pop(0)
    if line[:2] == ' 1':
        lines.pop(0)  # remove empty line
        break

    search_start = 0
    while True:
        stack_start = line.find('[', search_start)
        if stack_start == -1:
            break
        stack_no = stack_start // 4 + 1
        try:
            stacks[stack_no].insert(0, line[stack_start + 1])
        except KeyError:
            stacks[stack_no] = [line[stack_start + 1]]
        search_start = stack_start + 3

# Work on stacks
for line in lines:
    n_crates, stack_from, stack_to = [atoi(line.split()[i]) for i in [1, 3, 5]]
    crates = stacks[stack_from][-n_crates:]

    if ans == 1:
        crates.reverse()
    
    del stacks[stack_from][-n_crates:]
    stacks[stack_to] += crates

# Get top crates
keys = list(stacks.keys())
keys.sort()
top_crates = []
for key in keys:
    top_crates.append(stacks[key].pop())
print(f'Answer {ans}: ' + ''.join(top_crates))