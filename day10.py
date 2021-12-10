import re

with open('input\\day10') as f:
    puzzle_input = f.read().splitlines()

ERROR_POINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
COMPLETION_POINTS = {')': 1, ']': 2, '}': 3, '>': 4}
CLOSE_CHARS = {'(': ')', '[': ']', '{': '}', '<': '>'}
error_score = 0
completion_scores = []
for i, line in enumerate(puzzle_input):
    original = line
    while True:
        line, n = re.subn(r'(?:\{\})|(?:\[\])|(?:\(\))|(?:<>)', '', line, count=1)
        if n == 0: break
    if m := re.search(r'^[^)\}\]>]+([)\}\]>])', line):
        error, = m.groups(1)
        error_score += ERROR_POINTS[error]
    else:
        completion_strings = ''.join([CLOSE_CHARS[c] for c in line[::-1]])
        pscore = 0
        for c in completion_strings:
            pscore = pscore * 5 + COMPLETION_POINTS[c]
        completion_scores.append(pscore)

print('Part 1:', error_score)
print('Part 2:', sorted(completion_scores)[len(completion_scores)//2])