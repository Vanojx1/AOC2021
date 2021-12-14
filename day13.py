from point import Point

with open('input\\day13') as f:
    puzzle_input = f.read().splitlines()

dots = set([])
fold = []
for row in puzzle_input:
    if ',' in row:
        dots.add(Point(*map(int, row.split(','))))
    if 'fold' in row:
        axis, i = row.replace('fold along ', '').split('=')
        fold.append((axis, int(i)))

def print_paper(dots):
    MAX_X = max(map(lambda x: x.x, dots))
    MAX_Y = max(map(lambda x: x.y, dots))
    for y in range(MAX_Y+1): print(''.join(['#' if Point(x, y) in dots else ' ' for x in range(MAX_X+1)]))
    print()

for index, (axis, i) in enumerate(fold):

    # print_paper(dots)

    if axis == 'y':
        s1 = {d for d in dots if d.y < i}
        s2 = {d for d in dots if d.y > i}
        new_s2 = {Point(d.x, i-(d.y-i)) for d in s2}
        dots = s1 | new_s2
    else:
        s1 = {d for d in dots if d.x < i}
        s2 = {d for d in dots if d.x > i}
        new_s2 = {Point(i-(d.x-i), d.y) for d in s2}
        dots = s1 | new_s2

    if index == 0:
        print('Part 1:', len(dots))

print('Part 2:')
print_paper(dots)