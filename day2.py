from point import Point

with open('input\\day2') as f:
    puzzle_input = f.read().splitlines()

sub = Point(0, 0)

for m in puzzle_input:
    move, off = m.split(' ')
    if move == 'forward':
        sub += int(off)
    elif move == 'up':
        sub += Point(0, -int(off))
    elif move == 'down':
        sub += Point(0, int(off))
    else: raise Exception('BAD MOVE!')

print('Part 1:', sub.x * sub.y)

sub = Point(0, 0)
aim = 0

for m in puzzle_input:
    move, off = m.split(' ')
    if move == 'forward':
        sub += Point(int(off), int(off) * aim)
    elif move == 'up':
        aim -= int(off)
    elif move == 'down':
        aim += int(off)
    else: raise Exception('BAD MOVE!')

print('Part 2:', sub.x * sub.y)
