import re
from point import Point
from collections import Counter

with open('input\\day5') as f:
    puzzle_input = [list(map(int, re.match(r'(\d+),(\d+) -> (\d+),(\d+)', l).groups())) for l in f.read().splitlines()]

points = Counter()
for x1, y1, x2, y2 in puzzle_input:
    p1, p2 = sorted([Point(x1, y1), Point(x2, y2)])
    if p1.x == p2.x: points.update([(p1.x, y) for y in range(p1.y, p2.y+1)])
    elif p1.y == p2.y: points.update([(x, p1.y) for x in range(p1.x, p2.x+1)])

print('Part 1:', len([k for k, v in points.items() if v >= 2]))

points = Counter()
for i, (x1, y1, x2, y2) in enumerate(puzzle_input):
    p1, p2 = sorted([Point(x1, y1), Point(x2, y2)])
    if p1.x == p2.x: points.update([(p1.x, y) for y in range(p1.y, p2.y+1)])
    elif p1.y == p2.y: points.update([(x, p1.y) for x in range(p1.x, p2.x+1)])
    elif p2.x > p1.x: points.update([(p1.x+k, p1.y+k) for k in range(p2.y-p1.y+1)])
    else: points.update([(p1.x-k, p1.y+k) for k in range(p2.y-p1.y+1)])

# for y in range(10): print(''.join([str(points.get((x, y), '.')) for x in range(10)]))

print('Part 2:', len([k for k, v in points.items() if v >= 2]))