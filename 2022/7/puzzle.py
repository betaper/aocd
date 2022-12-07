# Standard library
import sys
from locale import atoi

# Local modules
import aocd

lines = aocd.read(sys.argv[1])


def parse_next_line():
    try:
        line = lines.pop(0)
    except IndexError:
        return None
    line = [arg.strip() for arg in line.split()]
    return line


# Parse commands
dirs = {'/': 0}
cd_name = '/'  # name of current directory
parse_line = True
while True:
    if parse_line is True:
        line = parse_next_line()
    else:
        parse_line = True

    if line is None:
        break

    if line[1] == 'cd':
        dir_name = line[2]
        if dir_name[0] != '/':  # relative dir
            if dir_name == '..':
                dir_name = cd_name.split('/')[1:-1]
                dir_name.pop()
                if dir_name == []:
                    dir_name = '/'
                else:
                    dir_name = '/' + '/'.join(dir_name) + '/'
            else:
                dir_name = cd_name + dir_name + '/'
        if dir_name not in dirs.keys():
            dirs[dir_name] = 0
        cd_name = dir_name

    if line[1] == 'ls':
        while True:
            line = parse_next_line()
            if line is None:
                break
            if line[0] == '$':
                parse_line = False
                break
            if line[0] == 'dir':
                pass
            else:
                dirs[cd_name] += atoi(line[0])

# Sort dirs according to number of subdirs
dir_names = list(dirs.keys())
s = [i[0] for i in sorted(enumerate(dir_names), key=lambda x: len(x[1]))]
dir_names = [dir_names[i] for i in s]

# Compute final directory sizes incl. sub-directories
while True:
    dir_name = dir_names.pop()
    if dir_name == '/':
        break
    if dir_name.count('/') > 2:
        parent = '/' + '/'.join(dir_name.split('/')[1:-2]) + '/'
        dirs[parent] += dirs[dir_name]
    else:
        dirs['/'] += dirs[dir_name]

total_size = sum([size for size in dirs.values() if size <= 100000])

dir_sizes = list(dirs.values())
min_size = max(dir_sizes) - 40000000
dir_size = min([size for size in dir_sizes if size > min_size])

print(f'Answer 1: {total_size}')
print(f'Answer 2: {dir_size}')