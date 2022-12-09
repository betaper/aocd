# Standard library
import sys
from locale import atoi
import numpy as np

# Local modules
import aocd


def move_knots(head, tail):
    sep = head - tail
    r, c = sep
    if abs(r) >= 2 or abs(c) >= 2:
        tail[0] += 1 if r > 0 else -1 if r < 0 else 0
        tail[1] += 1 if c > 0 else -1 if c < 0 else 0
    return tail


def show_visited(s):
    r_vals = [p[0] for p in s]
    c_vals = [p[1] for p in s]
    corners = [min(r_vals), max(r_vals), min(c_vals), max(c_vals)]
    n_rows = corners[1] - corners[0] + 1
    n_cols = corners[3] - corners[2] + 1
    image = np.full((n_rows, n_cols), '.')
    for p in s:
        im_row = p[0] - corners[0]
        im_col = p[1] - corners[2]
        image[im_row, im_col] = '#'
    # Mark start position
    r, c = -corners[0], -corners[2]
    image[r, c] = 's'
    for row in image:
        print(''.join(row))
    print(f'Start position: ({r}, {c})\n')


if __name__ == '__main__':
    show = False

    # Parse command-line arguments
    args = sys.argv
    for i, arg in enumerate(args):
        arg = arg.strip()
        if arg == '-s' or arg == '--show':
            show = True
            args.pop(i)
            break
    if len(args) < 3:
        print('Usage: python puzzle.py <input file> <number of knots> [-s | --show]')
        exit(1)

    lines = aocd.read(args[1])
    n_knots = atoi(args[2])

    knot = np.array([0, 0])
    rope = np.tile(knot, (n_knots, 1))
    move = {
        'R': np.array([0, 1]),
        'L': np.array([0, -1]),
        'U': np.array([-1, 0]),
        'D': np.array([1, 0])
    }
    visited = {(0, 0)}

    for line in lines:
        direction, steps = line.split()
        for step in range(atoi(steps)):
            rope[0, :] += move[direction]
            for i in range(n_knots - 1):
                rope[i + 1, :] = move_knots(rope[i, :], rope[i + 1, :])

            # update positions visited by tail
            visited.add(tuple(rope[-1, :]))

    # Simple graphical representation of positions visited by tail
    if show:
        show_visited(visited)

    print(f'Answer: {len(visited)}')
