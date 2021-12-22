from snailfish_num import SnailfishNum
from itertools import combinations

with open('input\\day18') as f:
    puzzle_input = f.read().splitlines()

n1 = puzzle_input[0]
for n2 in puzzle_input[1:]:
    str_add = f"[{n1},{n2}]"
    addition = list(str_add)
    snp = SnailfishNum(addition)
    while snp.reduce(): pass
    n1 = str(snp)

print('Part 1:', snp.magnitude)

max_magnitude = 0
for n1, n2 in combinations(puzzle_input, 2):
    str_add = f"[{n1},{n2}]"
    addition = list(str_add)
    snp = SnailfishNum(addition)
    while snp.reduce(): pass
    max_magnitude = max(max_magnitude, snp.magnitude)

print('Part 2:', max_magnitude)