from point import Point
from math import prod
from termcolor import colored

with open('input\\day9') as f:
    puzzle_input = f.read().splitlines()

cave_mapping = {Point(x, y): int(h) for y, row in enumerate(map(list, puzzle_input)) for x, h in enumerate(row)}

MAX_H = max(cave_mapping.values())

low_points = set([])
for loc, h in cave_mapping.items():
    if all(cave_mapping.get(loc+o, MAX_H) > h for o in (1, 1j, -1, -1j)):
        low_points.add(loc)

risk_level_sum = sum(map(lambda loc: cave_mapping.get(loc)+1, low_points))

print('Part 1:', risk_level_sum)

def generate_basins():
    for loc in low_points:
        q = [loc]
        visited = set([loc])
        while q:
            curr_pos = q.pop()

            for o in (1, 1j, -1, -1j):
                next_pos = curr_pos+o
                if next_pos in cave_mapping and \
                   next_pos not in visited and \
                   cave_mapping.get(next_pos) < 9:
                    q.append(next_pos)
                    visited.add(next_pos)
    
        yield visited

top_basins = sorted(generate_basins(), key=len)

top_3 = [len(b) for b in top_basins[-3:]]
print('Part 2:', prod(top_3))

MAX_SIZE = max(cave_mapping.keys())
draw_mapping = {(pos.x, pos.y): cave_mapping.get(pos) for basin in top_basins for pos in basin}
for y in range(MAX_SIZE.y+1): print(''.join([colored(draw_mapping[(x, y)], 'green') if (x, y) in draw_mapping else ' ' for x in range(MAX_SIZE.x+1)]))
